#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

import time

from classes.Tasks.BaseTask import BaseTask

class AddFriend(BaseTask):
    def __init__(self, vk):
        super().__init__(vk)
        self.delay = [5, 20]

    def exec(self):
        vk_api = self.vk.getConnect()

        self.users_list = ['41244707']

        if self.next_exec <= time.time():
            # response = vk_api.method('friends.add', {'user_id': self.users_list[0]})
            response = 200
            if 174 <= response <= 177:
                raise Exception('Ошибка добавления в друзья')
                # TODO log
            else:
                self.setNextExec()

        return 'success'

