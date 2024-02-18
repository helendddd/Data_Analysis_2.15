#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    with open("file4.txt", "w") as fileptr:
        fileptr.write(
            "Simple file\n"
        )
    # rename file2.txt to file3.txt
    os.rename("file4.txt", "file5.txt")

    # deleting the file named file3.txt
    os.remove("file5.txt")

    # creating a new directory with the name new
    os.mkdir("new")

    path = os.getcwd()
    print(path)
    # removing the new directory
    os.rmdir("new")
