import os
import sys
import argparse
from datetime import datetime

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

parser.add_argument(
    "-l",
    "--longformat",
    help="Shows more details about files -- mod time stamp, file size and file name",
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
    print_listing(args.dirname, args.filetype, args.longformat)


def print_listing(dirname, show_filetype, long_format):
    """
    Lists contents of a directory to stdout.
    :param dirname: A directory whose contents are to be listed.
    :param show_filetype: Boolean. Appends an extra character to file name showing its type.
    :param long_format: Boolean. Shows more information about files -- See -l flag."
    """
    files = get_directory_listing(dirname)
    assert type(files) == list
    if long_format:
        files = long_format_description(dirname, files, show_filetype)
    elif show_filetype:
        files = describe_files(dirname, files)

    # At this point, `files` contains each line of the desired output.

    # We know how this works
    for f in files:
        print(f)


def long_format_description(dirname, files, show_filetype):
    """
    :param dirname: Directory which contains the files.
    :param files: List of files in directory.
    :param d_files: List of files with extra descriptive character.
    :returns: List of full descriptor lines, one per file.
    """
    return [
        long_format_description_for_file(dirname, file, show_filetype) for file in files
    ]


def long_format_description_for_file(dirname, file, show_filetype):
    """
    (See `long_format_description`)
    :returns: A string giving the long format description of the file.
    """
    info_dict = file_info(dirname, file)
    mtime = info_dict["modtime"]
    filesize = info_dict["filesize"]
    filetype = info_dict["filetype"] if show_filetype else ""
    return f"{mtime} {filesize:>12} {file}{filetype}"


def file_info(dirname, file):
    """
    :param dirname: Directory containing file
    :param file: Name of file
    :returns: A dictionary of the form --
        {
           "modtime": "YYYY-MM-DD HH:MM:SS"
           "filesize": 35620287645,
           "filetype": "*"
        }
    """
    assert os.path.isdir(dirname)
    path = os.path.join(dirname, file)
    assert os.path.isfile(path) or os.path.isdir(path)

    # Directories are shown with 0 size in long format
    filesize = os.path.getsize(path) if os.path.isfile(path) else 0
    mtime = os.path.getmtime(path)
    mdt = datetime.fromtimestamp(mtime)
    mdt_formatted = mdt.strftime("%Y-%m-%d %H:%M:%S")

    info = {
        "modtime": mdt_formatted,
        "filesize": filesize,
        "filetype": filetype_char(dirname, file),
    }
    return info


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
