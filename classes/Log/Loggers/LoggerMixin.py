#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Exeptions.exeptions import NotOverrideMethodExeption

class LoggerMixin:
    def log(self, *args, **kwargs):
        raise NotOverrideMethodExeption('Do not overided method: error()')

    def error(self, *args, **kwargs):
        raise NotOverrideMethodExeption('Do not overided method: error()')

    def success(self, text):
        raise NotOverrideMethodExeption('Do not overided method: sucess()')