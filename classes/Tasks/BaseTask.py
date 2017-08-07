#!/usr/bin/python3
# -*- coding: utf-8 -*-

import abc
import random
import time

class BaseTask:
    def __init__(self, vk):
        self.vk = vk
        self.users_list = []
        self.next_exec = []
        self.delay = [0, 0]
        self.limit = 30
        self.next_exec = time.time()

    def getLimit(self):
        return self.limit

    def setLimit(self, limit):
        self.limit = limit

    def getDelay(self):
        return self.delay

    def setDelay(self, delay_from, delay_to):
        self.delay = [delay_from, delay_to]

    def setNextExec(self):
        currentDelay = random.randint(self.delay[0], self.delay[1])
        print(self.__class__.__name__ + ' Wait: ' + str(currentDelay))
        self.next_exec = time.time() + currentDelay

    def setUsersList(self, list):
        self.users_list = list

    @abc.abstractmethod
    def exec(self):
        pass


