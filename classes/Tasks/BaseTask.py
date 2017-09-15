#!/usr/bin/python3
# -*- coding: utf-8 -*-

import abc
import random
import time

from classes.Exeptions.exeptions import NotOverrideMethodExeption
from  classes.Instagram.InstaBot import InstaBot
from classes.Log.Log import Logger

class BaseTask:
    def __init__(self, insta):
        """:type insta: InstaBot"""
        self._tagsList = []
        self._insta = insta
        self._usersList = []
        self._next_exec = []
        self._delay = [35, 55]
        self._limit = 0
        self._showTime = False
        self._next_exec = time.time()

    def exec(self):
        if self.isDelayExpired() and not self.isLimitExpired():
            self.runTask()
        else:
            time.sleep(1)
            # self._showTime and Logger.loadingText('Осталось {} секунд'.format(round(self.getTimeLeft(), 0)))

    def runTask(self):
        raise NotOverrideMethodExeption('Do not overided method: runTask()')

    def getLimit(self):
        return self._limit

    def setLimit(self, limit):
        self._limit = limit
        return self

    def showTime(self):
        self._showTime = True
        return self

    def getDelay(self):
        return self._delay

    def setDelay(self, delay_from, delay_to):
        self._delay = [delay_from, delay_to]
        return self

    def isDelayExpired(self) -> bool:
        return self._next_exec <= time.time()

    def isLimitExpired(self) -> bool:
        return False

    def getTimeLeft(self):
        return self._next_exec - time.time()

    def setNextExec(self):
        currentDelay = random.randint(self._delay[0], self._delay[1])
        print(self.__class__.__name__ + ' Wait: ' + str(currentDelay))
        self._next_exec = time.time() + currentDelay

    def setUsersList(self, users):
        self._usersList = users
        return self

    def setTagsList(self, tags):
        self._tagsList = tags
        return self
