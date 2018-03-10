#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.UserSource.UserSourceContainer import UserSourceContainer

class UserSourceBuilder:
    __slots__ = {'typeContainer', 'userSource'}

    def __init__(self):
        self.typeContainer = UserSourceContainer()
        self.userSource = None

    def setType(self, type):
        self.userSource = self.typeContainer.getUserSource(type)
        return self

    def setSource(self, source, sourceType):
        self.userSource = self.userSource(source, type=sourceType)
        return self

    def setIsCycle(self, bool):
        self.userSource.isCycle(bool)
        return self

    def get(self):
        return self.userSource