#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk_api
from .constants import *


class VKConnecter():
    def __init__(self, login, password, token = None):
        self.login = login
        self.password = password
        self.token = token
        self.vk = self.connect()

    def connect(self):
        try:
            return vk_api.VkApi(self.login, self.password)  # Авторизируемся
        except vk_api.authorization_error as error_msg:
            print(error_msg)
            # TODO Log it

    def getConnect(self):
        return self.vk

    def bestWall(self, query = '', popul = 'likes:100', count = 200):
        vk = self.getConnect()
        q = popul + " " + query
        values = {'q': q, 'count': count}
        return vk.method('newsfeed.search', values)
