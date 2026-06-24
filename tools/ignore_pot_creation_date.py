import argparse
import logging
import os
import subprocess
import sys
import typing
import pathlib

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


def count_meaningful_changes(changeset: str, po_file: pathlib.Path) -> int:
    """
    Counts meaningful changes in the diff for a given PO file.
    """
    cmd = [
        "git",
        "diff",
        "--patch",
        "--unified=0",
        changeset,
        "--",
        os.fspath(po_file),
    ]
    output = subprocess.check_output(cmd, text=True)

    diff_lines = output.splitlines()
    return sum(
        1
        for line in diff_lines
        if (line.startswith("-") or line.startswith("+"))
        and "POT-Creation-Date:" not in line
        and "PO-Revision-Date:" not in line
        and str(po_file) not in line
    )


def revert_po_file(changeset, po_file: pathlib.Path) -> None:
    """
    Reverts a PO file to its original state in the given changeset.
    """
    # Use the first part of the changeset as the reference
    ref = changeset.split("...", 1)[0]
    logger = logging.getLogger(__name__)
    logger.info(f"{po_file} has no meaningful changes, reverting to {ref}")
    cmd = ["git", "show", f"{ref}:{po_file}"]
    output = subprocess.check_output(cmd, text=True)

    with po_file.open(mode="w") as file:
        file.write(output)


def main(argv: typing.Optional[typing.List[str]] = None) -> int:
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=logging.INFO
    )
    parser = argparse.ArgumentParser(
        description="Revert PO files with only timestamp changes."
    )
    parser.add_argument("--from-ref", help="Use changes since this commit.")
    parser.add_argument("--to-ref", help="Use changes until this commit.")
    parser.add_argument(
        "files", nargs="*", type=pathlib.Path, help="Only check these files."
    )
    args = parser.parse_args(argv)

    files_to_process = args.files if args.files else []

    changeset = get_git_changeset(args.from_ref, args.to_ref)

    for po_file in files_to_process:
        count = count_meaningful_changes(changeset, po_file)
        if count == 0:
            revert_po_file(changeset, po_file)

    return 0


if __name__ == "__main__":
    sys.exit(main())
