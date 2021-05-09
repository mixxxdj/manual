#!/usr/bin/env python3
import argparse
import tempfile
import shutil
from scour import scour

ARGS = (
    "--enable-comment-stripping",
    "--enable-id-stripping",
    "--enable-viewboxing",
    "--indent=none",
    "--no-line-breaks",
    "--remove-descriptions",
    "--remove-metadata",
    "--remove-titles",
)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="+")
    args = parser.parse_args(argv)
    options = scour.parse_args(list(ARGS))

    for input_file in args.input_file:
        with open(input_file, mode="rb") as input:
            with tempfile.NamedTemporaryFile(
                suffix=".svg", mode="wb", delete=False
            ) as output:
                scour.start(options, input, output)
        shutil.move(output.name, input_file)


if __name__ == "__main__":
    main()
