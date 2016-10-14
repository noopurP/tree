#! /usr/bin/env python
import sys
# -*- coding: UTF-8 -*-
import os
from os import listdir, sep
from os.path import abspath, basename, isdir, isfile
from sys import argv


def tree(dir, padding):
    content = os.listdir(dir)
    count = 0
    for f in content:
        count = count + 1
        if not f.startswith('.'):
            if count == len(content):
                print(padding + "└── " + f)
                if isdir(os.path.realpath(dir + '/' + f)):
                    padding = padding + "│   "
                    padding = tree(os.path.realpath(dir + '/' + f), padding)
                str = []
                str = padding.rpartition("│")
                padding = str[0]
                return padding
            else:
                print(padding + "├── " + f)
                if isdir(os.path.realpath(dir + '/' + f)):
                    padding = padding + "│   "
                    padding = tree(os.path.realpath(dir + '/' + f), padding)


def main():
    if len(sys.argv) == 1:
        path = os.getcwd()
        print(".")
        tree(path, ' ')
    else:
        path = os.path.realpath(sys.argv[1])
        print(sys.argv[1])
        tree(path, ' ')
if __name__ == '__main__':
    main()
