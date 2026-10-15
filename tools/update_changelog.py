#!/usr/bin/env python3
import argparse
import os

import requests


TEMPLATE = """
% This is a generated file. Do not edit it manually, because it is updated
% automatically via tools/update_changelog.py.

{content}"""


def fetch_changelog(branch):
    """Fetch CHANGELOG.md from branch of mixxxdj/mixxx repository."""
    r = requests.get(
        "https://raw.githubusercontent.com/mixxxdj/mixxx/"
        f"{branch}/CHANGELOG.md"
    )
    r.raise_for_status()
    return r.text


def changelog_apply_tmpl(changelog):
    """Apply the template to the changelog."""

    return TEMPLATE.lstrip().format(content=changelog)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--branch", required=True)
    args = parser.parse_args(argv)

    # Fetch changelog and convert to RST
    changelog = fetch_changelog(args.branch)
    changelog = changelog_apply_tmpl(changelog)

    # Write changelog to changelog.md file
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "../source/chapters/appendix/changelog.md",
    )
    with open(path, mode="w") as fp:
        fp.write(changelog)


if __name__ == "__main__":
    main()
