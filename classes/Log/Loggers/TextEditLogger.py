#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTextEdit

from classes.Log.Loggers.LoggerMixin import LoggerMixin

class TextEditLogger(LoggerMixin):
    def __init__(self, output):
        """"
        
        :type output: QTextEdit
        """
        self.output = output

    def log(self, text):
        self.output.setStyleSheet('''
            color: rgb(0, 0, 0);
        ''')
        self.output.append(text)

    def error(self, text):
        self.output.setStyleSheet('''
            color: rgb(200, 0, 0);
        ''')
        self.output.append(text)

    def success(self, text):
        self.output.setStyleSheet('''
            color: rgb(0, 200, 0);
        ''')
        self.output.append(text)