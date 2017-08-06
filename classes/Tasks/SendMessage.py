#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.MsgGenerator.MsgGenerator import MsgGenerator

class SendMessage:
    def __init__(self, vk):
        super().__init__()
        self.vk = vk
        self.users_list = []

    def getLimit(self):
        return self.limit

    def setLimit(self, limit):
        self.limit = limit

    def setUsersList(self, list):
        self.users_list = list

    def exec(self):
        vk_api = self.vk.getConnect()

        self.users_list = ['41244707']

        msgGen = MsgGenerator()
        for i in range(len(self.users_list)):
            params = {'user_id': self.users_list[i], 'message': msgGen.generate()}
            response = vk_api.method('messages.send', params)
            if 900 <= response <= 902:
                raise Exception('Ошибка отправки сообщения')
                # TODO log

        return 'success'

