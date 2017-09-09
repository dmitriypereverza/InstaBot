#!/usr/bin/python3
# -*- coding: utf-8 -*-

import abc
import random
import time
from  classes.Instagram.InstaBot import InstaBot
from classes.Log.LogClass import Logger

class BaseTask:
    def __init__(self, insta):
        """:type insta: InstaBot"""
        self.tagsList = []
        self.insta = insta
        self.usersList = []
        self.next_exec = []
        self.delay = [0, 0]
        self.limit = 30
        self.currentIndex = 0
        self.next_exec = time.time()

    def exec(self):
        if self.isDelayExpired() and not self.isLimitExpired():
            self.runTask()
        else:
            time.sleep(1)
            Logger.loadingText('Осталось {} секунд'.format(round(self.getTimeLeft(), 0)))

    @abc.abstractmethod
    def runTask(self):
        pass

    def getLimit(self):
        return self.limit

    def setLimit(self, limit):
        self.limit = limit
        return self

    def getDelay(self):
        return self.delay

    def setDelay(self, delay_from, delay_to):
        self.delay = [delay_from, delay_to]
        return self

    def isDelayExpired(self) -> bool:
        return self.next_exec <= time.time()

    def isLimitExpired(self) -> bool:
        return False

    def getTimeLeft(self):
        return self.next_exec - time.time()

    def setNextExec(self):
        currentDelay = random.randint(self.delay[0], self.delay[1])
        print(self.__class__.__name__ + ' Wait: ' + str(currentDelay))
        self.next_exec = time.time() + currentDelay

    def setUsersList(self, users):
        self.usersList = users
        return self

    def setTagsList(self, tags):
        self.tagsList = tags
        return self
