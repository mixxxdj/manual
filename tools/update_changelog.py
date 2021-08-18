#!/usr/bin/env python3
import argparse
import os
import re

import m2r2
import requests


TEMPLATE = """
.. This is a generated file. Do not edit it manually, because it is updated
   automatically via tools/update_changelog.py.

.. include:: /shortcuts.rstext

.. _appendix-version-history:

{content}

.. seealso:: For an overview of previous versions, `take a look
             <https://launchpad.net/mixxx/+series>`_ at the timeline.
"""


def fetch_changelog(branch):
    """ Fetch CHANGELOG.md from branch of mixxxdj/mixxx repository. """
    r = requests.get(
        "https://raw.githubusercontent.com/mixxxdj/mixxx/"
        f"{branch}/CHANGELOG.md"
    )
    r.raise_for_status()
    return r.text


def changelog_to_rst(changelog):
    """ Convert changelog to RST format used by sphinx. """
    # Replace headline with "Version History"
    changelog = re.sub(
        "^# Changelog$",
        "# Version History",
        changelog,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    # Ensure that all launchpad issues are hyperlinks
    changelog = re.sub(
        r"(?!\[)\blp:?(?P<lpid>\d+)\b(?!\])",
        r"[lp:\g<lpid>](https://bugs.launchpad.net/mixxx/+bug/\g<lpid>)",
        changelog,
    )

    # Ensure that all GitHub PRs are hyperlinks
    changelog = re.sub(
        r"(?!\[)#\b(?P<ghid>\d+)\b(?!\])",
        r"[#\g<ghid>](https://github.com/mixxxdj/mixxx/pull/\g<ghid>)",
        changelog,
    )

    return TEMPLATE.lstrip().format(content=m2r2.convert(changelog))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--branch", required=True)
    args = parser.parse_args(argv)

    # Fetch changelog and convert to RST
    changelog = fetch_changelog(args.branch)
    changelog = changelog_to_rst(changelog)

    # Write changelog to version_history.rst file
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "../source/chapters/appendix/version_history.rst",
    )
    with open(path, mode="w") as fp:
        fp.write(changelog)


if __name__ == "__main__":
    main()
