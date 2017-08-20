#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.TextGenerator.MsgGenerator import MsgGenerator
from classes.Tasks.BaseTask import BaseTask

class SendMessage(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [5, 20]

    def runTask(self):
        self.users_list = ['41244707']

        msgGen = MsgGenerator()
        for i in range(len(self.users_list)):
            params = {'user_id': self.users_list[i], 'message': msgGen.generate()}
            # response = vk_api.method('messages.send', params)
            response = 200
            if 900 <= response <= 902:
                raise Exception('Ошибка отправки сообщения')
                # TODO log
            else:
                self.setNextExec()


