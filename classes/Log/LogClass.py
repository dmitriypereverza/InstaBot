#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

class Logger:
    def log(text):
        print(text)

    def error(text):
        sys.stderr.write(bcolors.FAIL + text + bcolors.ENDC + '\n')

    def sucess(text):
        print(bcolors.OKBLUE + text + bcolors.ENDC + '\n')

    def warning(text):
        print(bcolors.WARNING + text + bcolors.ENDC + '\n')

    def loadingText(text):
        sys.stdout.write('\r' + text)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'