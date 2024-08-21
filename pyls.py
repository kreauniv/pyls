import os
import sys
import argparse


parser = argparse.ArgumentParser(
    prog="pyls", description="Lists contents of given directory or the pwd"
)

parser.add_argument(
    "dirname",
    action="store",
    help="Optional directory name to list.",
    nargs="?",
    default=".",
)


def main():
    """
    When given one argument, takes it to be a dirname and
    prints its listing. When given no arguments, assumes
    the directory being referred to is the current working
    directory.
    """
    args = parser.parse_args()
    print_listing(args.dirname)


def print_listing(dirname):
    """
    Lists contents of a directory to stdout.
    :param dirname: A directory whose contents are to be listed.
    """
    files = get_directory_listing(dirname)
    assert type(files) == list

    for f in files:
        print(f)


def get_directory_listing(dirname):
    """
    :param dirname: The directory whose contents are to be listed.
    :returns: A list of strings giving files and directories
    present in the given directory.
    """
    assert os.path.isdir(dirname), f"{dirname} is not a directory"

    return os.listdir(dirname)


if __name__ == "__main__":
    main()
