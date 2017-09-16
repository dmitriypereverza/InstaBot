#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Log.Loggers.LoggerMixin import LoggerMixin

class TextEditLogger(LoggerMixin):
    def __init__(self, logSendSignal):
        self._logSendSignal = logSendSignal

    def _sendLogHtmlText(self, text):
        self._logSendSignal.emit(text)

    def log(self, text):
        self._sendLogHtmlText("<span style='color:grey'>{}</span><br>".format(text))

    def error(self, text):
        self._sendLogHtmlText("<span style='color:red'>{}</span><br>".format(text))

    def success(self, text):
        self._sendLogHtmlText("<span style='color:green'>{}</span><br>".format(text))