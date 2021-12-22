import argparse
import datetime
import json
import time
import glob
from pathlib import Path
import os
import sys
import re
import hashlib
from typing import List, Tuple, Generator, Optional


from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.bagofwords import BagOfWords
from src.file_iter import iter_ndjson
from bin.bag_messages import Main as BagMain, append_filename


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "commit_file", type=str,
        help="ndjson of exported commit messages"
    )
    parser.add_argument(
        "--bags", type=str, default=["export/topic-bags-5"],
        help="paths to topic bag-of-words json files"
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
        help="Display stuff during run"
    )
    
    args = vars(parser.parse_args())

    return args


class Main:
    def __init__(
            self,
            commit_file: str,
            bags: List[str],
            verbose: bool,
    ):
        self.verbose = verbose
        self.commit_file = Path(commit_file)
        self.bag_file = append_filename(self.commit_file, "-big-bag.json")

        self.bigbag = BagOfWords.load_json(self.bag_file)
        self.bigbag_n = self.bigbag.normalized()
        self.topic_sets = dict()
        self.message_hashes = set()
        topic_bags = dict()

        for path in bags:
            for file in sorted(glob.glob(str(Path(path) / "*.json"))):
                name = Path(file).name.split(".")[0]
                if name.endswith("_r"):
                    continue
                if self.verbose:
                    print("loading", file)
                bag = BagOfWords.load_json(file)
                #bag = bag.normalized()
                #bag.subtract(self.bigbag_n, 4)
                topic_bags[name] = bag

        if not topic_bags:
            raise ValueError("No topic-bags found")

        orig_size = dict()
        self.topic_bags = dict()
        for name1, bag1 in topic_bags.items():
            orig_size[name1] = bag1.size()
            bag = bag1.copy()
            for name2, bag2 in topic_bags.items():
                if name1 != name2:
                    bag.subtract(bag2, bag1["to"] / bag2["to"] / len(topic_bags))

            self.topic_bags[name1] = bag

        for name, bag in self.topic_bags.items():
            self.topic_sets[name] = set(key for key, value in bag.items() if value > 5)
            if self.verbose:
                print(
                    f"{name:25}: {bag.size():8} / {orig_size[name]:8}",
                    ", ".join(list(bag.sort().bag.keys())[:10])
                )
        #self.topic_bags["politics"].dump()
        input()
        self.run()

    def run(self):
        for i, (commit, message, message_n) in enumerate(self.iter_commits(desc="scanning messages", min_length=1000)):
            bag = BagOfWords(message_n)
            if bag.size() < 30:
                continue

            rows = []
            bag_set = set(bag.bag)
            for topic, topic_set in self.topic_sets.items():
                intersection = topic_set & bag_set
                intersection_length = len(intersection)
                if intersection_length > 1:
                    rows.append([topic, intersection_length, intersection_length / bag.size(), intersection])
            rows.sort(key=lambda r: -r[1])

            if rows and rows[0][0] in (
                    #"fuck",
                    #"personal",
                    #"loving",
                    #"code", "fixed", "curse", "segfault", "oops",
                    #"emotion",
                    #"corona",
                    "music",
                    #"amazing",
                    #"facebook",
                    #"repo_spiral",
                    #"curse"
                    #"politics",
            ) and rows[0][2] >= 0.3:
                print(f"\n\n{commit['date']} {commit['repo']}/commit/{commit['sha']} {commit['author']}\n")
                print(message_n)
                print(f"\n{'message:':20} {bag.size():6,} / 1.0")
                for topic, size, ratio, intersection in rows:
                    print(
                        f"{topic + ':':20} {size:6,} / {str(round(ratio, 3)):7}"
                        f" / {', '.join(sorted(intersection))}"
                    )

    def iter_commits(self, desc: str, min_length: Optional[int] = None) -> Generator[Tuple[dict, str, str], None, None]:
        iterable = iter_ndjson(self.commit_file)
        if self.verbose:
            iterable = tqdm(iterable, desc=desc)

        for commit in iterable:
            if "[bot]" in commit["author"]:
                continue

            message = commit["message"].strip()
            if min_length and len(message) < min_length:
                continue

            hash = hashlib.md5(message.encode("utf-8")).hexdigest()
            if hash in self.message_hashes:
                continue
            self.message_hashes.add(hash)

            message_n = BagMain.normalize_text(message)

            if BagMain.skip_message(message_n):
                continue

            yield commit, message, message_n


if __name__ == "__main__":
    Main(**parse_args())
