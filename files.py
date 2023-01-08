from typing import List
import os.path
import glob


def two_lists_files(path: str, exp: str, flag: bool) -> List:
    res = [[], []]
    for root, dirs, files in os.walk(path):
        if flag is True:
            for file in files:
                if file.split('.')[1] == exp:
                    res[0].append(file)
            for dir in dirs:
                res[1].append(dir)
        if flag is False:
            for i in glob.glob(f"{path}/*.{exp}"):
                if os.path.split(i)[1] not in res[0]:
                    res[0].append(os.path.split(i)[1])
            for f in dirs:
                if os.path.isdir(os.path.join(path, f)):
                    res[1].append(f)

    return res[0]
