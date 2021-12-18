import re
import json
import hashlib
from pathlib import Path
from typing import Optional

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
    RE_HEX_START = re.compile(r"^[a-f0-9]+")

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.processed_shas = set()
        self.commits = []
        self.word_counter = dict()
        self.stats = {
            "num_events": 0,
            "num_push_events": 0,
            "num_commit_messages": 0,
            "num_commit_characters": 0,
        }
        self.written_hashes = set()

    def dump_stats(self):
        msg = (
            f"\ncommits:               {len(self.commits)}"
            f"\nmax rank:              {self.commits[0]['rank'] if self.commits else 0}"
        )
        for key, value in self.stats.items():
            msg += f"\n{key+':':22} {value:,d}"
        print(msg)

    def process_event(self, event: dict):
        self.stats["num_events"] += 1
        if event["type"] != "PushEvent":
            return

        self.stats["num_push_events"] += 1

        for commit in event["payload"]["commits"]:
            self.stats["num_commit_messages"] += 1
            self.stats["num_commit_characters"] += len(commit["message"])

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

            exclude_msg = self.process_commit(event, commit)
            if exclude_msg and self.verbose:
                print(f'\nEXCLUDE: {event["repo"]["name"]}/commit/{commit["sha"]} - {exclude_msg}')

    def process_commit(self, event: dict, commit: dict) -> Optional[str]:
        message = commit["message"]
        if not message:
            return

        if "[bot]" in commit["author"]["email"]:
            return

        # TODO: it's a bit radical but guess that no good message
        #   starts like this
        if message.lstrip().startswith("Squashed '"):
            return "Starts with <Squashed '>"

        for ignore_string in self.IGNORE_THESE:
            if ignore_string in message:
                return f"Ignored because of string '{ignore_string}'"

        if len(message) < 50:
            return  # f"Too short {len(message)}"

        message_hash = hashlib.sha256(commit["message"].encode("utf-8")).hexdigest()
        if message_hash in self.written_hashes:
            return  # "Skip already repeating message hash"

        # sometimes there's just a lot of random characters
        #   without spaces. that also excludes chinese texts
        #   but they usually won't have much english words for ranking
        num_spaces = len([c for c in message if c == " "])
        if num_spaces / len(message) < 1 / 100:
            return  # f"Not enough spaces {num_spaces}/{len(message)}"

        message = self.normalize_message(message)

        rank = 0
        matched_words = []
        for weight, words in WEIGHTED_WORDS.items():
            for word in words:
                if isinstance(word, str):
                    is_match = word in message
                    if is_match:
                        matched_words.append(word)
                else:
                    matches = word.findall(message)
                    is_match = bool(matches)
                    if is_match:
                        matched_words.append(matches[0])
                if is_match:
                    rank += weight

        if rank < 10:
            return  # f"Rank too low: {rank}"

        exclude_msg = self.has_too_much_repetitive_line_starts(message)
        if exclude_msg:
            return exclude_msg

        self.written_hashes.add(message_hash)
        self.commits.append({
            "date": event["created_at"],
            "repo": event["repo"]["name"],
            "rank": rank,
            "matched_words": sorted(matched_words),
            "commit": commit,
            "hash": message_hash,
        })
        self.commits.sort(key=lambda c: c["rank"], reverse=True)
        if len(self.commits) > 100:
            self.commits.pop(-1)

        for word in message.split():
            self.word_counter[word] = self.word_counter.get(word, 0) + 1

    def store_stash(self, filename: Path):
        filename.write_text(json.dumps({
            "stats": self.stats,
            "commits": self.commits,
        }, indent=2))

    def load_stash(self, filename: Path):
        data = json.loads(filename.read_text())
        self.stats = data["stats"]
        self.commits = data["commits"]

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

    @classmethod
    def has_too_much_repetitive_line_starts(cls, message: str, max_count: int = 10) -> Optional[str]:
        count = dict()
        for line in message.splitlines():
            line = line.lstrip()

            hex_start = cls.RE_HEX_START.findall(line)
            if hex_start and len(hex_start[0]) >= 8:
                # from the regex we can not be sure if it's really a hex number
                #   so we check if it's more than max_count of
                #   'possible' hex-values of the same length
                tag = f"hex-{len(hex_start[0])}"
            else:
                tag = line[:6]

            # TODO: generally messages with a lot of '* ' entries are boring
            #   this might miss the creative ones but it's hard to distinguish
            #   at this level
            if tag.startswith("* "):
                tag = "*"
            if tag.strip() and not tag.startswith("http") and not tag.startswith("```"):
                count[tag] = count.get(tag, 0) + 1

        if any(v > max_count for v in count.values()):
            count = {
                key: count[key]
                for key in sorted(count, key=lambda k: count[k], reverse=True)
                if count[key] > max_count
            }
            return f"Too many repetitive line starts: {count}"

    def render_markdown(self) -> str:
        md_commits = [
            self.commit_to_markdown(commit)
            for commit in sorted(
                self.commits,
                key=lambda c: c["date"],
            )
        ]
        return "\n---\n".join(md_commits)

    def render_stats_markdown(self) -> str:
        return (
            f'{self.stats["num_events"]:,d} events'
            f', {self.stats["num_push_events"]:,d} push events'
            f', {self.stats["num_commit_messages"]:,d} commit messages'
            f', {self.stats["num_commit_characters"]:,d} characters'
        ) + "\n"

    @classmethod
    def commit_to_markdown(cls, commit: dict) -> str:
        md = (
            f'## [{commit["repo"]}](https://github.com/{commit["repo"]})@'
            f'[{commit["commit"]["sha"][:10]}...]'
            f'(https://github.com/{commit["repo"]}/commit/{commit["commit"]["sha"]})'
            f'\n#### {commit["date"].replace("T", " ").replace("Z", "")}'
            f' by {commit["commit"]["author"]["name"]}'
        )
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
