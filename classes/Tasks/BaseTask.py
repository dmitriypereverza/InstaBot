#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import time

from classes.Exeptions.exeptions import NotOverrideMethodExeption, EmptyUserListExeption
from classes.Instagram.InstaBot import InstaBot
from classes.Instagram.instaUser import User
from classes.TextGenerator.BaseCommentGenerator import BaseCommentGenerator
from classes.UserSource.UserSources import BaseUserSource

class BaseTask:
    def __init__(self, insta):
        """:type insta: InstaBot"""
        self._insta = insta
        self._usersSource = None
        self._commentGenerator = None
        self._needComment = False
        self._needFollow = False
        self._likeSettings = []
        self._next_exec = []
        self._delay = [35, 55]
        self._limit = 0
        self._showTime = False
        self._next_exec = time.time()

    def exec(self):
        if self.isDelayExpired() and not self.isLimitExpired():
            user = self.getUserSource().getNext()
            if not user:
                raise EmptyUserListExeption()
            self.runTask(user)
        else:
            time.sleep(1)

    def runTask(self, user: User):
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

    def setUserSource(self, userSource: BaseUserSource):
        self._usersSource = userSource
        self._usersSource.setInstaConnect(self._insta)
        return self

    def getUserSource(self) -> BaseUserSource:
        return self._usersSource

    def setLikeSettings(self, settings):
        self._likeSettings = settings
        return self

    def getLikeSettings(self):
        return self._likeSettings

    def needComment(self, *args):
        if len(args) > 0:
            self._needComment = args[0]
            return self
        else:
            return self._needComment

    def needFollow(self, *args):
        if len(args) > 0:
            self._needFollow = args[0]
            return self
        else:
            return self._needFollow

    def setCommentGenerator(self, commentGenerator: BaseCommentGenerator):
        self._commentGenerator = commentGenerator
        return self

    def getCommentGenerator(self) -> BaseCommentGenerator:
        return self._commentGenerator