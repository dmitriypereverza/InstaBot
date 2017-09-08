#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Logger:
    def log(text):
        print(text)

    def error(text):
        print(bcolors.FAIL + text + bcolors.ENDC)

    def sucess(text):
        print(bcolors.OKBLUE + text + bcolors.ENDC)

    def warning(text):
        print(bcolors.WARNING + text + bcolors.ENDC)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'