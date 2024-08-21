from pyls import *
import stat
import os
from datetime import datetime


def create_file(filename):
    with open(filename, "w") as f:
        f.write("sample file")


def with_setup(fn):
    # Setup
    create_file("ordinary.txt")
    create_file("executable")
    os.mkdir("testdir")
    os.chmod("executable", stat.S_IRWXO + stat.S_IRWXG + stat.S_IRWXU)
    try:
        # Tests
        fn()
    finally:
        # Teardown
        os.remove("ordinary.txt")
        os.remove("executable")
        os.removedirs("testdir")


def test_filetype_char():
    def check():
        assert "*" == filetype_char(
            ".", "executable"
        ), "Suffix character for executables is '*'"
        assert "/" == filetype_char(
            ".", "testdir"
        ), "Suffix character for directories is '/'"
        assert "" == filetype_char(
            ".", "ordinary.txt"
        ), "No suffix character for ordinary files"

    with_setup(check)


def test_file_info():
    d = datetime.now().timestamp()
    f = datetime.fromtimestamp(d).strftime("%Y-%m-%d %H:%M:%S")

    def check():
        os.utime("ordinary.txt", times=(d, d))
        os.utime("executable", times=(d, d))
        filesize = 11
        info = file_info(".", "ordinary.txt")
        assert info["modtime"] == f
        assert info["filesize"] == filesize
        assert info["filetype"] == ""
        info = file_info(".", "executable")
        assert info["modtime"] == f
        assert info["filesize"] == filesize
        assert info["filetype"] == "*"
        info = file_info(".", "testdir")
        assert info["filesize"] == 0
        assert info["filetype"] == "/"

    with_setup(check)


def test_long_format():
    d = datetime.now().timestamp()
    f = datetime.fromtimestamp(d).strftime("%Y-%m-%d %H:%M:%S")

    def check():
        os.utime("ordinary.txt", times=(d, d))
        os.utime("executable", times=(d, d))
        filesize = 11
        info = long_format_description_for_file(".", "ordinary.txt", True)
        assert info == f"{f} {filesize:>12} ordinary.txt"
        info = long_format_description_for_file(".", "executable", True)
        assert info == f"{f} {filesize:>12} executable*"

    with_setup(check)
