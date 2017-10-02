#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint
import re

from classes.TextGenerator.BaseCommentGenerator import BaseCommentGenerator

class MsgGenerator(BaseCommentGenerator):
    TYPE_LIST = 'list'
    TYPE_FILE = 'file'

    def __init__(self, template_list, type='list'):
        if type == self.TYPE_LIST:
            self.list = template_list
        if type == self.TYPE_FILE:
            self.list = self._getListFromFile(template_list)

    def generate(self, username = ''):
        strResult = self.getRandomTamplate()
        strResult = re.sub('\|', '~~', strResult)
        matches = re.findall(r"{.*?}", strResult)
        for i in range(len(matches)):
            groupedMatches = re.findall(r"([^\~\~\{\}]+)", matches[i])
            strResult = re.sub(R'{}'.format(matches[i]), groupedMatches[randint(0, len(groupedMatches) - 1)], strResult)

        strResult = self.insertUserName(strResult, username)

        return strResult

    def getRandomTamplate(self):
        return self.list[randint(0, len(self.list) - 1)]

    def insertUserName(self, strResult, username):
        if username:
            username = ' @' + username
        return re.sub(R'%username%', username, strResult)

    def _getListFromFile(self, filePath):
        try:
            with open(filePath, 'r') as f:
                output = f.readlines()
        except FileNotFoundError:
            output = []

        return [x.strip() for x in output]