#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle

class Scheduler:
    def __init__(self):
        self.list_tasks = []

    def addTask(self, task):
        self.list_tasks.append(task)
        return self

    def enableTaskLoop(self):
        self.list_tasks = cycle(self.list_tasks)
        return self

    def start(self):
        for task in self.list_tasks:
            task.exec()

