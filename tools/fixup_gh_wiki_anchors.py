#!/usr/bin/env python3
import argparse
import re

URL_REGEX = (
    r"(?P<url>https?:\/\/github.com\/\S*\/\S*\/wiki\/\S*)\#"
    r"(?:user-content-)?(?P<anchor>\S*)"
)
URL_SUB = r"\g<url>#user-content-\g<anchor>"


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="+")
    args = parser.parse_args(argv)
    for filepath in args.input_file:
        with open(filepath, "r") as file:
            file_content = file.read()
        subbed = re.sub(URL_REGEX, URL_SUB, file_content)
        with open(filepath, "w") as file:
            file.write(subbed)


if __name__ == "__main__":
    main()
