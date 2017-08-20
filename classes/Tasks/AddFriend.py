#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class AddFriend(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [5, 20]

    def runTask(self):

        for user in self.users_list:
            self.insta.follow(user.id)
        response = 200
        if 174 <= response <= 177:
            raise Exception('Ошибка добавления в друзья')
            # TODO log
        else:
            self.setNextExec()