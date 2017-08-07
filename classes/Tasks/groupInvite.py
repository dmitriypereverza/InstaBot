#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class groupInvite(BaseTask):
    def __init__(self, vk):
        super().__init__(vk)

    def exec(self):
        vk_api = self.vk.getConnect()

        group = '41244707'
        self.users_list = ['41244707']

        response = vk_api.method('friends.add', {
            'group_id': group,
            'user_id': self.users_list[0],
        })
        if 174 <= response <= 177:
            raise Exception('Ошибка добавления в друзья')
            # TODO log

        return 'success'

