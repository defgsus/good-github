import argparse
import datetime
import json
from pathlib import Path
import os
from typing import List

from tqdm import tqdm

from src.gharchive import GHArchive
from src.good_messages import GoodMessages
from src.update_index import update_index, get_message_files


ROOT_DIR = Path(__file__).resolve().parent


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "days", type=str, nargs="*",
        help="Days to scan, either YYYY[-MM[-DD]] or 'yesterday'"
    )
    parser.add_argument(
        "--path", type=str, nargs="?", default="gharchive-dump",
        help="The path where to store the event ndjson files (needs a lot of space!)"
    )
    parser.add_argument(
        "-f", "--force", type=bool, nargs="?", default=False, const=True,
        help="Force re-generation of the markdown files, even if existing",
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, nargs="?", default=False, const=True,
        help="Display stuff during run"
    )
    
    args = vars(parser.parse_args())

    days = set()
    for day in args["days"]:
        if day == "yesterday":
            days.add(datetime.date.today() - datetime.timedelta(days=1))
        else:
            if len(day) == 10:
                days.add(datetime.datetime.strptime(day, "%Y-%m-%d").date())
            elif len(day) == 7:
                date = datetime.datetime.strptime(day, "%Y-%m").date()
                month = date.month
                while date.month == month:
                    days.add(date)
                    date += datetime.timedelta(days=1)
            elif len(day) == 4:
                date = datetime.datetime.strptime(day, "%Y").date()
                year = date.year
                while date.year == year:
                    days.add(date)
                    date += datetime.timedelta(days=1)
            else:
                raise ValueError(f"Invalid date '{day}'")

    args["days"] = sorted(days)
    return args


def main(
        days: List[datetime.date],
        path: str,
        verbose: bool,
        force: bool,
):
    existing_files = get_message_files()
    existing_dates = [
        datetime.date(int(d[0]), int(d[1].lstrip("0")), int(d[2].lstrip("0")))
        for d, fn in existing_files
    ]

    archive = GHArchive(
        raw_path=path,
        verbose=verbose,
    )
    for day in days:

        if not force:
            if day in existing_dates:
                if verbose:
                    print(f"Skipping {day}, use -f to overwrite")
                continue

        proc = GoodMessages(verbose=verbose)

        stash_file = (ROOT_DIR / "stash" / str(day)[:4] / f"{str(day)[:10]}.json")

        key_interrupt = False
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
            key_interrupt = True

        if not stash_file.parent.exists():
            os.makedirs(stash_file.parent)
        proc.store_stash(stash_file)
        proc.store_words(stash_file.parent / f"{str(day)[:10]}-words.json")

        proc.remove_duplicates()

        if verbose:
            print(len(proc.commits), "commits")

        md_file = (ROOT_DIR / "docs" / "good-messages" / str(day)[:4] / f"{str(day)[:10]}.md")
        if not md_file.parent.exists():
            os.makedirs(md_file.parent)
        md_file.write_text(
            f"# {str(day)[:10]}\n\n"
            + proc.render_stats_markdown() + "\n\n"
            + proc.render_markdown()
        )

        if key_interrupt:
            break

    update_index(verbose=verbose)


if __name__ == "__main__":
    main(**parse_args())
