import json
import gzip
import glob
import csv
import io
from pathlib import Path
from typing import Union, Generator, IO


def iter_ndjson(file: Union[str, Path, IO], raise_error: bool = False, skip: int = 0) -> Generator[dict, None, None]:
    for line in iter_lines(file, skip=skip):
        try:
            yield json.loads(line)
        except json.JSONDecodeError as e:
            if raise_error:
                raise
            print(f"\n\nJSON ERROR '{e}' for line '{line}'\n")


def iter_csv(file: Union[str, Path, IO], skip: int = 0) -> Generator[dict, None, None]:
    iterable = iter_lines(file, skip=skip, keep_first=True)
    reader = csv.DictReader(iterable)
    yield from reader


def iter_lines(file: Union[str, Path, IO], skip: int = 0, keep_first: bool = False) -> Generator[dict, None, None]:
    if isinstance(file, (str, Path)):
        filename = str(file)

        if "*" in filename or "?" in filename:
            if skip:
                raise ValueError("globbing and 'skip' currently not supported")
            for fn in sorted(glob.glob(filename)):
                yield from iter_lines(fn)

        else:
            if filename.lower().endswith(".gz"):
                with io.TextIOWrapper(io.BufferedReader(gzip.open(filename))) as fp:
                    count = 0
                    for line in fp:
                        if skip and count < skip:
                            count += 1
                            if keep_first and count == 1:
                                yield line
                            continue

                        yield line

            else:
                with open(file, "rt") as fp:
                    yield from iter_lines(fp, skip=skip)

    else:
        count = 0
        for line in file.readlines():
            if skip and count and count < skip:
                count += 1
                if keep_first and count == 1:
                    yield line
                continue

            yield line


def iter_file(file: Union[str, Path], skip: int = 0) -> Generator[dict, None, None]:
    filename = str(file).lower()
    if filename.endswith(".csv") or filename.endswith(".csv.gz"):
        yield from iter_csv(file, skip=skip)

    elif filename.endswith(".ndjson") or filename.endswith(".ndjson.gz"):
        yield from iter_ndjson(file, skip=skip)

    else:
        raise ValueError(f"Unsupported file format for '{file}'")
