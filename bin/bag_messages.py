import argparse
import datetime
import json
import time
from pathlib import Path
import os
import sys
import re
from typing import List, Tuple, Generator


from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.bagofwords import BagOfWords
from src.file_iter import iter_ndjson


RE_REPLACE_WHITESPACE = (
    # urls
    re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&#+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"),
    # emails
    re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
    # long hex numbers like commit refs
    re.compile(r"[a-f0-9]{30,1000}"),
)

USELESS_MESSAGE_TAILS = (
    "Merge pull request",
    "Signed-off-by:",
    "Commit reference:",
    "Sync branch \"",
    "Authored-by:",
    "Co-authored-by:",
    "Reported-by:",
    "Acked-by:",
    "Reviewed By:",
    "Merged PRs:",
    "Excluded PRs:",
    "Merge branch '",
    "Merge remote-tracking branch '",
    "Deploying to gh-pages from @",
    "This is an automated commit",
    "Set up CI with Azure Pipelines\n",
    "Source-Link: http",
    "Change log: http",
    "issuer signature:",
    "*By submitting this pull request, I confirm",
    "# All SDK Contribution checklist:",  # Azure SDK
    "Update Composer dependencies (",
    "--BEGIN PGP SIGNATURE--",
)

TOPICS = [
    (
        "game", "shotgun", "sprite", "missile", "witch", "witches", "zombie", "zombies",
        "spaceship", "spaceships", "demon", "demons", "player", "players", "player's",
        "joystick", "spawn", "spawned", "spawning", "respawning", "dragon",
        "lair", "monster", "monsters", "survivor", "assassin", "assassins",
        "billiard", "shooter", "knight", "knights", "knight's", "projectile",
        "damage", "minecraft", "bukkit", "spigot", "multiplayer",
        "explosive", "hostile", "gameloop", "grenade",
    ),
    (
        "emotion", "sadness", "pain", "depression", "depressed",
        "despair", "desperation", "loving", "frustrating", "frustration",
        "paranoia", "forgiving", "suffering",
    ),
    (
        "fun", "funny", "hilarious", "ridiculous", "joke", "joking",
        "laugh", "laughing", "kidding",
    ),
    (
        "music", "musical", "song", "melody", ""
    ),
    (
        "code", "function", "refactor", "kernel", "status", "thread", "settings",
        "threads", "maintenance", "synchronisation", "revision",
        "function", "functions", "variable", "variables", "upstream", "implementation",
        "driver", "struct", "cleanup", "issues", "fixes", "process", "processing", "buffer", "module",
        "command", "cpu", "arm64", "documentation", "reference", "align", "pointer",
        "architecture", "server", "hardware", "compiler", "directory", "register",
        "integration", "deployment", "inline", "coverage", "recursive", "dependencies",
        "compilation", "bytes", "bits", "generator", "functional", "compatibility",
        "extension", "instructions", "operation", "management", "interrupt", "macro",
        "syntax", "initialization", "install", "overflow", "merged", "endpoint", "pipeline",
    ),
    (
        "blog", "article"
    ),
    ("fixed", "fixes", "fixing"),
    "microsoft", "apple", "amazon", "facebook",
    "segfault",
    ("css", "scss", "html", "http", "javascript"),
    ("amazing", "superb", "stunning", "excellent", "inspiring", "superb"),
    (
        "curse", "cursed", "damn", "awful", "hate", "hated", "disgusting", "bloody",
        "silly", "silliness", "stupid", "stupidity", "terrible",
        "shit", "shitty", "bullshit", "suck", "sucks", "sucking", "sucker"
        "fuck", "fucking", "fucked", "fuckoff", "fuckyou",
    ),
    (
        "politics", "government", "governments", "governmental", "politics", "political"
    ),
    (
        "oops", "ah", "aah", "oh", "ohh", "woah"
    ),
    (
        "corona", "pandemic",
    ),
    (
        "tanh", "tan", "sin", "asin", "sinh", "cos", "acos", "cosh", "tan", "tanh", "sqrt",
        "ceil",
    )
]

TOPICS_3 = [
    ("honest", "honestly", "frankly"),
    ("amazing", "superb", "stunning", "excellent", "inspiring"),
    ("shit", "shitty", "bullshit"),
    ("depressed", "depression", "depressive", "depressing"),
    ("code", "coding", "programming"),
    ("confess", "confessing", "confession"),
    ("idea", "ideas", "inspiration", "inspiring"),
    "feedback",
]

TOPICS_2 = [
    "female", "male",
    "girl", "boy",
    "girlfriend", "boyfriend",
    "sister", "brother",
    "college", "school",
    ("mystery", "mysteries"),
    ("friend", "friends"),
    ("dream", "dreams", "dreamy"),
    "thoughts", "grief",
    "tears",
    ("criminal", "criminals"),
    "antifa",
    ("sex", "sexual"),
    (),
    ("fuck", "fucking", "fucked", "fuckoff", "fuckyou"),
    ("corona", "pandemic", "covid"),
    "personal",

    ("god", "gods"),
    ("hell", "hellish", "hellfire"),
    ("guitar", "saxophone", "banjo", "ukulele", "flute"),
    ("praise", "praised"),
    ("church", "churches"),
    "love", "hate", "hatred",
    "loving",
    ("fire", "fires"),
    "kernel",
    "python",
]


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "commit_file", type=str,
        help="ndjson of exported commit messages"
    )
    parser.add_argument(
        "--repos", type=str, nargs="+",
        help="Instead of the topic-bags, build one for each repo",
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
        help="Display stuff during run"
    )
    
    args = vars(parser.parse_args())

    return args


def append_filename(filename: Path, suffix: str) -> Path:
    name = filename.name
    if name.lower().endswith(".gz"):
        name = name[:-3]

    name_parts = name.split(".")
    name = ".".join(name_parts[:-1])

    name = name + suffix

    return filename.parent / name


class Main:
    def __init__(
            self,
            commit_file: str,
            repos: List[str],
            verbose: bool,
    ):
        self.commit_file = Path(commit_file)
        self.bag_file = append_filename(self.commit_file, "-big-bag.json")
        self.commit_bag_file = append_filename(self.commit_file, "-bags.ndjson")
        self.verbose = verbose
        self.repos = repos

        if self.bag_file.exists():
            self.bag = BagOfWords.load_json(self.bag_file)
        else:
            self.bag = self.render_bag()
            self.bag.save_json(self.bag_file)
        self.bag_norm = self.bag.normalized()

        print(f"bag: {self.bag.size():,} / {self.bag.count():,}")

        self.topic_bags = dict()
        if not self.repos:
            for topic in sorted(TOPICS, key=lambda t: t[0] if isinstance(t, tuple) else t):
                if isinstance(topic, str):
                    topic = [topic]
                for suffix in ("", "_r"):
                    self.topic_bags[topic[0] + suffix] = {
                        "tokens": topic,
                        "bag": BagOfWords()
                    }
        else:
            for repo in self.repos:
                name = repo.replace("/", "-")
                self.topic_bags[name] = {
                    "repo": repo,
                    "bag": BagOfWords()
                }
        self.scan_commits()

    @classmethod
    def normalize_text(cls, text: str) -> str:
        for useless_tail in USELESS_MESSAGE_TAILS:
            try:
                idx = text.index(useless_tail)
                text = text[:idx]
            except ValueError:
                pass
        text = text.lower()
        for repl in RE_REPLACE_WHITESPACE:
            text = repl.sub(" ", text)
        text = text.replace("\n", " ").replace("\r", " ")
        return text

    @classmethod
    def skip_message(cls, text: str) -> bool:
        if not text:
            return True

        for char, min_avg_space in (
                # exclude file listings
                ("/", 40),
                # exclude other weird stuff
                ("(", 60),
                ("[", 60),
                (".", 40),
                (">", 60),
        ):
            ratio = text.count(char) / len(text)
            if ratio >= 1. / min_avg_space:
                return True

        return False

    def iter_commits(self, desc: str) -> Generator[Tuple[dict, str, str], None, None]:
        iterable = iter_ndjson(self.commit_file)
        if self.verbose:
            iterable = tqdm(iterable, desc=desc)

        for i, commit in enumerate(iterable):

            if self.repos:
                found = False
                for repo in self.repos:
                    if ("/" in repo and commit["repo"] == repo) or (commit["repo"].endswith("/" + repo)):
                        found = True
                        break
                if not found:
                    continue

            if "[bot]" in commit["author"]:
                continue

            message = commit["message"]
            message_n = self.normalize_text(message)

            if self.skip_message(message_n):
                continue

            yield commit, message, message_n

    def render_bag(self) -> BagOfWords:
        big_bag = BagOfWords()
        num_bytes_written = 0

        def dump_stats():
            print()
            print(
                f"\ndate:      {commit['date']}"
                f"\ntokens:    {big_bag.size():,} / {big_bag.count():,}"
                f"\nwritten:   {num_bytes_written:,}"
                "\n"
            )

        for i, (commit, message, message_n) in enumerate(self.iter_commits(desc="creating big bag-of-words")):
            big_bag += message_n
            #bag = BagOfWords(message_n)
            #big_bag += bag

            #commit.pop("message")
            #commit["bag"] = bag.bag
            #num_bytes_written += fp.write(json.dumps(commit) + "\n")

            if self.verbose and i % 300_000 == 0:
                dump_stats()

        if self.verbose:
            dump_stats()

        return big_bag

    def scan_commits(self):
        try:
            self._scan_commits_topic()
        except KeyboardInterrupt:
            pass

        self._save_topic_bags()

    def _save_topic_bags(self):
        path = Path(__file__).resolve().parent.parent / "export" / "topic-bags"
        os.makedirs(path, exist_ok=True)
        for topic, bag in self.topic_bags.items():
            bag["bag"].save_json(path / f"{topic}.json")

    def _scan_commits_topic(self):
        def dump_stats():
            msg = f"\n\ndate:      {commit['date']}\n"
            for token, bag in self.topic_bags.items():
                if not token.endswith("_r") or self.repos:
                    msg += f"{token+':':20}"
                msg += f" {bag['bag'].size():10,d} / {bag['bag'].count():10,d}"
                if token.endswith("_r") or self.repos:
                    msg += "\n"
            print(msg)

        last_print_time = time.time()
        last_save_time = time.time()
        for i, (commit, message, message_n) in enumerate(self.iter_commits(desc="building topic bags")):

            bag = BagOfWords(message_n)
            subset = None
            for topic, topic_bag in self.topic_bags.items():
                if self.repos:
                    if (
                            ("/" in topic_bag["repo"] and commit["repo"] == topic_bag["repo"])
                            or (commit["repo"].endswith("/" + topic_bag["repo"]))
                    ):
                        topic_bag["bag"] += bag

                else:
                    found = False
                    for t in topic_bag["tokens"]:
                        if t in bag.bag:
                            found = True
                            break
                    if not found:
                        continue

                    if topic.endswith("_r"):
                        if subset is None:
                            subset = bag.get_subset(
                                self.bag_norm,
                                max_freq=0.03,
                                min_freq_mult=20,
                            )
                        for key in subset:
                            topic_bag["bag"].add_word(key)
                    else:
                        for key in bag.bag:
                            topic_bag["bag"].add_word(key)

            cur_time = time.time()
            if self.verbose and cur_time - last_print_time > 10:
                last_print_time = cur_time
                dump_stats()

            if cur_time - last_save_time > 60:
                last_save_time = cur_time
                self._save_topic_bags()

        if self.verbose:
            dump_stats()


if __name__ == "__main__":
    Main(**parse_args())
