import re
import glob
import json
import datetime
from pathlib import Path
from typing import List, Tuple


PROJECT_PATH = Path(__file__).resolve().parent.parent
DOCS_PATH = PROJECT_PATH / "docs"
TEMPLATE_PATH = PROJECT_PATH / "templates"
MESSAGES_PATH = DOCS_PATH / "good-messages"


MessageFiles = List[Tuple[Tuple[str, str, str], Path]]


def update_index(verbose: bool):
    files = get_message_files()
    if verbose:
        print("writing", DOCS_PATH / "messages.md")
    update_messages_index_markdown(files)
    if verbose:
        print("writing", MESSAGES_PATH / "index.json")
    update_messages_index_json(files)
    if verbose:
        print("writing", PROJECT_PATH / "README.md")
    update_readme(files)


def update_readme(files: MessageFiles):
    date = "-".join(files[-1][0])
    messages = (DOCS_PATH / files[-1][1]).read_text()

    # strip the header and footer with the relative links
    messages = messages.strip()
    messages = messages[messages.index("\n")+1:]
    messages = messages[:messages.rindex("\n")].rstrip()
    messages = f"# [{date}](docs/{files[-1][1]})\n\n" + messages + "\n"

    md = (TEMPLATE_PATH / "README.md").read_text()
    md %= {"date": date, "messages": messages}
    (PROJECT_PATH / "README.md").write_text(md)


def update_messages_index_markdown(files: MessageFiles):
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

        md += f"[{date[2]}]({filename})\n"

    md += "\n"

    Path(DOCS_PATH / "messages.md").write_text(md)


def update_messages_index_json(files: MessageFiles):
    RE_MESSAGE_TITLE = re.compile(r"^##\s\[[\w\d/_\-]+\]\(https://github.com/.*\)@", re.MULTILINE)

    index = []
    for date, filename in files:
        md = (DOCS_PATH / filename).read_text()
        repos = RE_MESSAGE_TITLE.findall(md)
        index.append({
            "date": "-".join(date),
            "num_messages": len(repos),
        })

    Path(MESSAGES_PATH / "index.json").write_text(json.dumps({"index": index}))


def get_message_files() -> MessageFiles:
    files = []
    for filename in glob.glob(str(MESSAGES_PATH / "????" / "????-??-??.md")):
        filename = Path(filename)

        rel_path = filename.relative_to(DOCS_PATH)
        name = filename.name
        date = (name[:4], name[5:7], name[8:10])
        files.append((date, rel_path))

    files.sort()
    return files
