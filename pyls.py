import os
import sys


def main(argv):
    """
    When given one argument, takes it to be a dirname and
    prints its listing. When given no arguments, assumes
    the directory being referred to is the current working
    directory.
    """
    if len(argv) > 0:
        dirname = argv[0]
    else:
        dirname = "."
    print_listing(dirname)


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
    main(sys.argv[1:])
