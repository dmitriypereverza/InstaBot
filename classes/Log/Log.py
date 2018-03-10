#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit
from classes.DecoHelpers.classDecorators import singleton
from classes.Log.Loggers.ConsoleLogger import ConsoleLogger
from classes.Log.Loggers.LoggerMixin import LoggerMixin

@singleton
class Logger():
    """
    
    :type logger: QTextEdit
    """
    def __init__(self):
        self.logger = ConsoleLogger()

    def setLoggerType(self, logger: LoggerMixin):
        self.logger = logger
        return self

    def log(self, *args, **kwargs):
        self.logger.log(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def success(self, *args, **kwargs):
        self.logger.success(*args, **kwargs)