from pathlib import Path
import glob
import os
import warnings
import datetime
from typing import Union, Generator, List, Optional

import requests
from tqdm import tqdm

from .file_iter import iter_ndjson


class GHArchive:

    def __init__(
            self,
            raw_path: Union[str, Path],
            verbose: bool = True,
    ):
        self.raw_path = Path(raw_path)
        self.verbose = verbose

    def iter_events(
            self,
            day: datetime.date,
    ) -> Generator[dict, None, None]:
        id_set = set()

        for hour in range(0, 24):
            filename = self.get_event_file(day, hour)
            if not filename:
                continue

            for event in iter_ndjson(filename):

                # skip the old events
                if not event.get("id"):
                    warnings.warn("Old events (without id) are skipped a.t.m.")
                    continue

                if event["id"] not in id_set:
                    yield event
                    id_set.add(event["id"])

                    # remove the oldest IDs
                    if len(id_set) >= 1_000_000:
                        for id in sorted(id_set)[:500_000]:
                            id_set.remove(id)

    def get_event_file(self, day: datetime.date, hour: int) -> Optional[Path]:
        filename = f"{day.year}-{day.month:02d}-{day.day:02d}-{hour}.json.gz"
        local_filename = self.raw_path / f"{day.year}" / filename
        if not local_filename.exists():
            if not self._download(filename, local_filename):
                return
        return local_filename

    def _download(self, filename: str, local_filename: Path, chunk_size: int = 64_000) -> bool:
        with requests.get(f"https://data.gharchive.org/{filename}", stream=True) as r:
            if r.status_code != 200:
                if self.verbose:
                    print(f"\n\nNOT FOUND {r.request.url}, got status {r.status_code}")
                return False

            size = int(r.headers['content-length'])
            iterable = r.iter_content(chunk_size=chunk_size)
            if self.verbose:
                iterable = tqdm(iterable, total=size // chunk_size, desc=f"downloading {filename}")
            try:
                with open(str(local_filename), "wb") as fp:
                    for data in iterable:
                        fp.write(data)
                return True
            except:
                # don't leave half files
                os.remove(str(local_filename))
                raise

    @staticmethod
    def _sort_key(k: str):
        idx = k.rfind(os.sep) + 1
        if k[idx+12] == ".":
            return k[:idx+11] + "0" + k[idx+11:]
        return k
