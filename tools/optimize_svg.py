#!/usr/bin/env python3
import argparse
import concurrent.futures
import multiprocessing
import tempfile
import shutil
from scour import scour

OPTIONS = scour.parse_args(
    [
        "--enable-comment-stripping",
        "--enable-id-stripping",
        "--enable-viewboxing",
        "--indent=none",
        "--no-line-breaks",
        "--remove-descriptive-elements",
    ]
)


def optimize_file(input_file):
    with open(input_file, mode="rb") as input:
        with tempfile.NamedTemporaryFile(
            suffix=".svg", mode="wb", delete=False
        ) as output:
            scour.start(OPTIONS, input, output)
    shutil.move(output.name, input_file)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="+")
    parser.add_argument(
        "-j", "--jobs", type=int, default=multiprocessing.cpu_count()
    )
    args = parser.parse_args(argv)
    max_workers = args.jobs
    print(f"Using {max_workers} concurrent jobs.")
    with concurrent.futures.ProcessPoolExecutor(max_workers) as executor:
        executor.map(optimize_file, args.input_file)


if __name__ == "__main__":
    main()
