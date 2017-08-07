#!/usr/bin/python3
# -*- coding: utf-8 -*-

class BotAnket():
    def __init__(self):
        self.list_tasks = []

    def addTask(self, task):
        self.list_tasks.append(task)

    def start(self):
        for task in self.list_tasks:
            task.exec()

