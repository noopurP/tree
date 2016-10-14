#! /usr/bin/env python
import sys
# -*- coding: UTF-8 -*-
import os
from os import listdir, sep
from os.path import abspath, basename, isdir, isfile
from sys import argv
global totdir, totfil


def tree(dir, padding):
    global totdir
    global totfil
    content = os.listdir(dir)
    count = 0
    for f in content:
        count = count + 1
        if not f.startswith('.'):
            if count != len(content):
                print(padding + "├── " + f)
                if isdir(os.path.realpath(dir + '/' + f)):
                    global totdir
                    totdir = totdir + 1
                    padding = padding + "│   "
                    padding = tree(os.path.realpath(dir + '/' + f), padding)
                else:
                    global totfil
                    totfil = totfil + 1
            else:
                print(padding + "└── " + f)
                if isdir(os.path.realpath(dir + '/' + f)):
                    global totdir
                    totdir = totdir + 1
                    padding = padding + "   "
                    padding = tree(os.path.realpath(dir + '/' + f), padding)
                else:
                    global totfil
                    totfil = totfil + 1
                str = []
                str = padding.rpartition("│")
                padding = str[0]
                return padding


if __name__ == '__main__':
    global totdir
    global totfil
    totdir = 0
    totfil =0
    if len(sys.argv) <= 1:
        print(".")
        tree(".", '')
    else:
        path = os.path.realpath(sys.argv[1])
        print(sys.argv[1])
        tree(path, '')
    print("")
    print(totdir, "directories,", totfil, "files")
