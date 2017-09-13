#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Exeptions.exeptions import NotOverrideMethodExeption

class RequestHandlerMixin:
    def get(self, *args, **kwargs):
        raise NotOverrideMethodExeption('Do not overided method: get()')

    def headersUpdate(self, *args, **kwargs):
        raise NotOverrideMethodExeption('Do not overided method: headersUpdate()')

    def post(self, *args, **kwargs):
        raise NotOverrideMethodExeption('Do not overided method: post()')

    def getJson(self, url):
        raise NotOverrideMethodExeption('Do not overided method: getJson()')