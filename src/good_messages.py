import re
import json
from pathlib import Path

from .words import WEIGHTED_WORDS


class GoodMessages:

    # ignore messages that contain these strings
    IGNORE_THESE = [
        # This is just getting on my nerves
        "or you for me Camilo Sasuke Thomas Borregaard Sørensen!!"
    ]

    # repos that generally fit the word search
    #   but do not really contain interesting messages
    IGNORE_REPOS = [
        "fbi-most-wanted-scraper",
    ]

    RE_TO_WHITESPACE = re.compile(r"[,.!?:\-'\"()[\]{}]")
    RE_LSTRIP_HEX = re.compile(r"^[a-f0-9]+\s*")

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.processed_shas = set()
        self.commits = []
        self.word_counter = dict()

    def dump_stats(self):
        print(
            f"\ncommits:  {len(self.commits)}"
            f"\nmax rank: {self.commits[0]['rank'] if self.commits else 0}"
        )

    def process_event(self, event: dict):
        if event["type"] != "PushEvent":
            return

        for ignore_repo in self.IGNORE_REPOS:
            if "/" in ignore_repo:
                if event["repo"]["name"] == ignore_repo:
                    return
            else:
                if event["repo"]["name"].split("/")[-1] == ignore_repo:
                    return

        for commit in event["payload"]["commits"]:

            if commit["sha"] in self.processed_shas:
                continue
            self.processed_shas.add(commit["sha"])

            self.process_commit(event, commit)

    def process_commit(self, event: dict, commit: dict):
        if "[bot]" in commit["author"]["email"]:
            return

        message = commit["message"]

        # it's a bit radical but guess that no real commit message
        #   starts like this
        if message.lstrip().startswith("Squashed '"):
            return

        for ingore_string in self.IGNORE_THESE:
            if ingore_string in message:
                return

        if len(message) < 100:
            return

        message = self.normalize_message(message)

        rank = 0
        for weight, words in WEIGHTED_WORDS.items():
            for word in words:
                if isinstance(word, str):
                    is_match = word in message
                else:
                    is_match = bool(word.findall(message))
                if is_match:
                    rank += weight

        if rank < 10:
            return

        if self.has_too_much_repetitive_line_starts(message):
            return

        self.commits.append({
            "repo": event["repo"]["name"],
            "commit": commit,
            "date": event["created_at"],
            "rank": rank,
        })
        self.commits.sort(key=lambda c: c["rank"], reverse=True)
        if len(self.commits) > 100:
            self.commits.pop(-1)

        for word in message.split():
            self.word_counter[word] = self.word_counter.get(word, 0) + 1

    def store_words(self, filename: Path):
        wc = {
            w: self.word_counter[w]
            for w in sorted(sorted(self.word_counter), key=lambda w: self.word_counter[w], reverse=True)
        }
        filename.write_text(json.dumps(wc, indent=2))

    @classmethod
    def normalize_message(cls, message: str) -> str:
        message = " " + cls.RE_TO_WHITESPACE.sub(" ", message.lower())
        return message

    def has_too_much_repetitive_line_starts(self, message: str) -> bool:
        count = dict()
        for line in message.splitlines():
            tag = line.lstrip()[:6]
            if tag.startswith("* "):
                tag = "*"
            if tag.strip() and not tag.startswith("http") and not tag.startswith("```"):
                count[tag] = count.get(tag, 0) + 1

                tag2 = self.RE_LSTRIP_HEX.sub(" ", tag)
                if tag2 != tag and tag2.strip():
                    count[tag2] = count.get(tag2, 0) + 1

        if any(v > 10 for v in count.values()):
            if self.verbose:
                count = {
                    key: count[key]
                    for key in sorted(count, key=lambda k: count[k], reverse=True)
                    if count[key] > 10
                }
                print("\n\nTOO MANY REPETITIVE LINE STARTS", count)
            return True
        return False

    def render_markdown(self) -> str:
        md_commits = [
            self.commit_to_markdown(commit)
            for commit in sorted(
                self.commits,
                key=lambda c: c["date"],
            )
        ]
        return "\n---\n".join(md_commits)

    @classmethod
    def commit_to_markdown(cls, commit: dict) -> str:
        #md = f'# [{commit["repo"]}](https://github.com/{commit["repo"]}/commit/{commit["commit"]["sha"]})\n\n'
        md = f'## [{commit["repo"]}](https://github.com/{commit["repo"]}/)\n'
        md += f'##### {commit["date"].replace("T", " ").replace("Z", "")}' \
              f' [{commit["commit"]["sha"][:10]}...]' \
              f'(https://github.com/{commit["repo"]}/commit/{commit["commit"]["sha"]})' \
              f' by {commit["commit"]["author"]["name"]}'
        md += "\n\n"
        md += commit["commit"]["message"]
        if not md.endswith("\n"):
            md += "\n"
        return md

    def remove_duplicates(self):
        def _middle(m: str) -> str:
            q = len(m) // 4
            return m[q:-q]

        to_remove = set()
        for i, c1 in enumerate(self.commits):
            m1 = c1["commit"]["message"]
            for j, c2 in enumerate(self.commits[i+1:]):
                j = i + j + 1
                m2 = c2["commit"]["message"]
                if m1 == m2 or _middle(m1) in m2 or _middle(m2) in m1:
                    to_remove.add(j)

        self.commits = [
            c for i, c in enumerate(self.commits)
            if i not in to_remove
        ]