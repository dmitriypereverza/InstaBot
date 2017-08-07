#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import random

from classes.TextGenerator.MsgGenerator import MsgGenerator
from classes.Tasks.BaseTask import BaseTask

class SendMessage(BaseTask):
    def __init__(self, vk):
        super().__init__(vk)
        self.delay = [5, 20]

    def exec(self):
        vk_api = self.vk.getConnect()

        self.users_list = ['41244707']

        msgGen = MsgGenerator()

        if self.next_exec <= time.time():
            for i in range(len(self.users_list)):
                params = {'user_id': self.users_list[i], 'message': msgGen.generate()}
                # response = vk_api.method('messages.send', params)
                response = 200
                if 900 <= response <= 902:
                    raise Exception('Ошибка отправки сообщения')
                    # TODO log
                else:
                    self.setNextExec()

        return 'success'

