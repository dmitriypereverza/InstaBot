#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from classes.Log.Loggers.LoggerMixin import LoggerMixin

class ConsoleLogger(LoggerMixin):
    def log(self, text):
        print(text)

    def error(self, text):
        sys.stderr.write(bcolors.FAIL + text + bcolors.ENDC + '\n')

    def success(self, text):
        print(bcolors.OKBLUE + text + bcolors.ENDC + '\n')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'