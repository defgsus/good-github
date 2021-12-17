import glob
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
        print("writing docs/messages.md")
    update_messages_index(files)
    if verbose:
        print("writing README.md")
    update_readme(files)


def update_readme(files: MessageFiles):
    date = "-".join(files[-1][0])
    messages = (DOCS_PATH / files[-1][1]).read_text()

    # strip the header with the relative links
    messages = messages.lstrip()
    messages = messages[messages.index("\n")+1:]
    messages = f"# [{date}](docs/{files[-1][1]})\n\n" + messages

    md = (TEMPLATE_PATH / "README.md").read_text()
    md %= {"date": date, "messages": messages}
    (PROJECT_PATH / "README.md").write_text(md)


def update_messages_index(files: MessageFiles):
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
