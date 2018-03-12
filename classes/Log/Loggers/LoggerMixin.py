#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Exeptions.exeptions import NotOverrideMethodExeption

class LoggerMixin:
    def log(self, *args, **kwargs):
        raise NotOverrideMethodExeption()

    def error(self, *args, **kwargs):
        raise NotOverrideMethodExeption()

    def success(self, text):
        raise NotOverrideMethodExeption()