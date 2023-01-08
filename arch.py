from zipfile import ZipFile
from files import two_lists_files
import os


def archive_file(name, exp):
    
    dirname = os.getcwd()
    files = two_lists_files(dirname, exp, False)
    for f in files:
        with ZipFile(name, "a") as testzip:
            testzip.write(f)


archive_file("test.zip", "txt")
