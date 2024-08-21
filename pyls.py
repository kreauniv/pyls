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

parser.add_argument(
    "-F",
    "--filetype",
    help="Describes file type by appending an extra character at end of file name.",
    action="store_true",
)


def main():
    """
    When given one argument, takes it to be a dirname and
    prints its listing. When given no arguments, assumes
    the directory being referred to is the current working
    directory.
    """
    args = parser.parse_args()
    print_listing(args.dirname, args.filetype)


def print_listing(dirname, show_filetype):
    """
    Lists contents of a directory to stdout.
    :param dirname: A directory whose contents are to be listed.
    :param show_filetype: Appends an extra character to file name showing its type.
    """
    files = get_directory_listing(dirname)
    assert type(files) == list
    if show_filetype:
        files = describe_files(dirname, files)

    for f in files:
        print(f)


def describe_files(dirname, files):
    """
    :param dirname: Take the directory whose listing is given in `files`.
    :param files: List of files in `dirname`.
    :returns: List of files with extra character at end that captures file type.
    Uses '*' for executables and '/' for directories.
    """
    assert os.path.isdir(dirname)

    return [describe_file(dirname, filename) for filename in files]


def describe_file(dirname, filename):
    """
    (See `describe_files` - but for one file)
    """
    return filename + filetype_char(dirname, filename)


def filetype_char(dirname, filename):
    """
    (See `describe_files`)
    """
    fullpath = os.path.join(dirname, filename)
    if os.path.isdir(fullpath):
        return "/"
    if os.access(fullpath, os.X_OK):
        return "*"
    return ""


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
