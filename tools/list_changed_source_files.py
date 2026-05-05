import os
import subprocess
import sys

SOURCE_SUFFIXES = {".rst", ".md"}


def get_changed_source_files() -> list[str]:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    if event_name != "pull_request":
        return []

    baseCommitSHA = os.environ.get("PR_BASE_SHA", "")
    if not baseCommitSHA or baseCommitSHA == "0" * 40:
        return []

    filesDifferFromBaseCommit = subprocess.run(
        # "source/" matches all subdirectories recursively
        ["git", "diff", "--name-only", baseCommitSHA, "HEAD", "--", "source/"],
        capture_output=True,
        text=True,
        check=True,
    )

    return [
        line
        for line in filesDifferFromBaseCommit.stdout.splitlines()
        if any(line.endswith(suffix) for suffix in SOURCE_SUFFIXES)
    ]


def main() -> None:
    files = get_changed_source_files()
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"files={' '.join(files)}\n")

    if files:
        print(f"Changed source files: {files}")
    else:
        print("No source files changed.")

    sys.exit(0)


if __name__ == "__main__":
    main()
