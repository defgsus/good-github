import argparse
import datetime
import json
from pathlib import Path
import os
import sys
from typing import List

from tqdm import tqdm

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.gharchive import GHArchive


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "days", type=str, nargs="*",
        help="Days to export, either YYYY[-MM[-DD]] or 'yesterday'"
    )
    parser.add_argument(
        "-o", "--output", type=str, nargs="?", default="export/messages/",
        help="path where to store the commits/messages",
    )
    parser.add_argument(
        "--path", type=str, nargs="?", default="gharchive-dump",
        help="The path where to store the event ndjson files (needs a lot of space!)"
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
        output: str,
        path: str,
        verbose: bool,
):
    output = Path(output)
    if not output.exists():
        os.makedirs(output)

    commits_file = (output / "commits.ndjson").open("wt")
    num_commits = 0
    num_bytes_written = 0

    def dump_stats():
        print()
        print(
            f"\ndate:    {event['created_at']}"
            f"\ncommits: {num_commits:,d}"
            f"\nwritten: {num_bytes_written:,d}"
        )

    archive = GHArchive(
        raw_path=path,
        verbose=verbose,
    )
    for day in days:

        iterable = archive.iter_events(day, event_type="PushEvent")
        if verbose:
            iterable = tqdm(iterable, desc=f"parsing events {str(day)[:10]}")

        for i, event in enumerate(iterable):

            if event["type"] == "PushEvent":
                for commit in event["payload"]["commits"]:
                    export_text = json.dumps({
                        "date": event["created_at"],
                        "repo": event["repo"]["name"],
                        "author": commit["author"]["name"],
                        "sha": commit["sha"],
                        "message": commit["message"],
                    }) + "\n"
                    num_bytes_written += commits_file.write(export_text)
                    num_commits += 1

            if verbose and i % 100_000 == 0:
                dump_stats()

    commits_file.close()
    dump_stats()


if __name__ == "__main__":
    main(**parse_args())
