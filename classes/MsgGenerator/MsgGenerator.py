#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

class MsgGenerator:
    def __init__(self):
        self.list = []

    def generate(self):
        self.list = ['Привет', 'Рандомная фраза', 'Test1', 'Test3', 'Test2']

        return self.list[randint(0, len(self.list) - 1)]