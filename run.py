import argparse
import datetime
import json
from pathlib import Path
import os

from tqdm import tqdm

from src.gharchive import GHArchive
from src.good_messages import GoodMessages


ROOT_DIR = Path(__file__).resolve().parent


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "day", type=str, 
        help="Day to inspect, either YYYY-MM-DD or 'yesterday'"
    )
    parser.add_argument(
        "path", type=str,
        help="The path where to store the event ndjson files"
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
        help="Display stuff during run"
    )
    
    args = vars(parser.parse_args())
    
    if args["day"] == "yesterday":
        args["day"] = datetime.date.today() - datetime.timedelta(days=1)
    else:
        args["day"] = datetime.datetime.strptime(args["day"], "%Y-%m-%d")
    
    return args


def main(
        day: datetime.date,
        path: str,
        verbose: bool,
):
    archive = GHArchive(
        raw_path=path,
        verbose=verbose,
    )
    proc = GoodMessages(verbose=verbose)

    stash_file = (ROOT_DIR / "stash" / str(day)[:4] / f"{str(day)[:10]}.json")

    if 1:
        try:
            iterable = archive.iter_events(day)
            if verbose:
                iterable = tqdm(iterable, desc=f"parsing events {str(day)[:10]}")

            for i, event in enumerate(iterable):
                proc.process_event(event)

                if verbose and i % 100_000 == 0:
                    print()
                    proc.dump_stats()

        except KeyboardInterrupt:
            pass

        if not stash_file.parent.exists():
            os.makedirs(stash_file.parent)
        proc.store_stash(stash_file)
        proc.store_words(stash_file.parent / f"{str(day)[:10]}-words.json")

    else:
        proc.load_stash(stash_file)

    proc.remove_duplicates()

    if verbose:
        print(len(proc.commits), "commits")

    md_file = (ROOT_DIR / "docs" / str(day)[:4] / f"{str(day)[:10]}.md")
    if not md_file.parent.exists():
        os.makedirs(md_file.parent)
    md_file.write_text(
        f"# *good github* {str(day)[:10]}\n\n"
        + proc.render_stats_markdown() + "\n\n"
        + proc.render_markdown()
    )


if __name__ == "__main__":
    main(**parse_args())
