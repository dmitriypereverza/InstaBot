#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class AddFriend(BaseTask):
    def __init__(self, vk):
        super().__init__(vk)
        self.delay = [5, 20]

    def runTask(self, vk_api):
        self.users_list = ['41244707']

        # response = vk_api.method('friends.add', {'user_id': self.users_list[0]})
        response = 200
        if 174 <= response <= 177:
            raise Exception('Ошибка добавления в друзья')
            # TODO log
        else:
            self.setNextExec()