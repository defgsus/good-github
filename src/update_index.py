import glob
import datetime
from pathlib import Path

DOCS_PATH = Path(__file__).resolve().parent.parent / "docs"


def update_index():

    messages_path = DOCS_PATH / "good-messages"

    files = []
    for filename in glob.glob(str(messages_path / "????" / "????-??-??.md")):
        filename = Path(filename)

        rel_path = filename.relative_to(DOCS_PATH)
        name = filename.name
        date = (name[:4], name[5:7], name[8:10])
        files.append((date, rel_path))

    files.sort()

    md = ""
    year = None
    month = None
    for date, filename in files:
        if date[0] != year:
            year = date[0]
            md += f"\n\n### {year}\n\n"
        if date[1] != month:
            month = date[1]
            md += f"\n\n#### {datetime.date(2000, int(month.lstrip('0')), 1).strftime('%B')}\n\n"

        md += f"[{date[2]}]({filename}) "

    md += "\n"

    Path(DOCS_PATH / "messages.md").write_text(md)
