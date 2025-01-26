import argparse
import logging
import os
import subprocess
import sys
import typing

"""
This script reverts changes in PO files when only the timestamp has changed.
It helps to create meaningful commits by ignoring unnecessary changes.
"""


def get_git_changeset(from_ref, to_ref) -> str:
    """
    Constructs the changeset string for `git diff` based on from_ref and
    to_ref.
    """
    from_ref = (
        from_ref
        or os.getenv("PRE_COMMIT_FROM_REF")
        or os.getenv("PRE_COMMIT_SOURCE")
        or "HEAD"
    )
    to_ref = (
        to_ref
        or os.getenv("PRE_COMMIT_TO_REF")
        or os.getenv("PRE_COMMIT_ORIGIN")
    )
    return f"{from_ref}...{to_ref}" if to_ref else from_ref


def count_meaningful_changes(changeset, po_file) -> int:
    """
    Counts meaningful changes in the diff for a given PO file.
    """
    cmd = ["git", "diff", "--patch", "--unified=0", changeset, "--", po_file]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    proc.check_returncode()

    diff_lines = proc.stdout.splitlines()
    return sum(
        1
        for line in diff_lines
        if (line.startswith("-") or line.startswith("+"))
        and "POT-Creation-Date:" not in line
        and "PO-Revision-Date:" not in line
        and po_file not in line
    )


def revert_po_file(changeset, po_file, logger):
    """
    Reverts a PO file to its original state in the given changeset.
    """
    ref = changeset.split("...")[
        0
    ]  # Use the first part of the changeset as the reference
    logger.info(f"{po_file} has no meaningful changes, reverting to {ref}")
    cmd = ["git", "show", f"{ref}:{po_file}"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    proc.check_returncode()

    with open(po_file, "w") as file:
        file.write(proc.stdout)


def main(argv: typing.Optional[typing.List[str]] = None) -> int:
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="Revert PO files with only timestamp changes."
    )
    parser.add_argument("--from-ref", help="Use changes since this commit.")
    parser.add_argument("--to-ref", help="Use changes until this commit.")
    parser.add_argument("files", nargs="*", help="Only check these files.")
    args = parser.parse_args(argv)

    # Remove the first entry which is the script file name itself
    files_to_process = args.files[1:] if args.files else []

    changeset = get_git_changeset(args.from_ref, args.to_ref)

    for po_file in files_to_process:
        count = count_meaningful_changes(changeset, po_file)
        if count == 0:
            revert_po_file(changeset, po_file, logger)

    return 0


if __name__ == "__main__":
    sys.exit(main())
