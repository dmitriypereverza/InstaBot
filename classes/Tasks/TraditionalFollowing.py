#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class TraditionalFollowing(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]
        self.tagIndex = 0
        self.tagPostIndex = 0

    def runTask(self):
        usersList = self.usersList



        self.setNextExec()

    def getNextTag(self):
        pass