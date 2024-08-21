from pyls import *
import stat
import os


def create_file(filename):
    with open(filename, "w") as f:
        f.write("sample file")


def test_filetype_char():
    create_file("ordinary.txt")
    create_file("executable")
    os.mkdir("testdir")
    os.chmod("executable", stat.S_IRWXO + stat.S_IRWXG + stat.S_IRWXU)
    try:
        assert "*" == filetype_char(
            ".", "executable"
        ), "Suffix character for executables is '*'"
        assert "/" == filetype_char(
            ".", "testdir"
        ), "Suffix character for directories is '/'"
        assert "" == filetype_char(
            ".", "ordinary.txt"
        ), "No suffix character for ordinary files"
    finally:
        os.remove("ordinary.txt")
        os.remove("executable")
        os.removedirs("testdir")
