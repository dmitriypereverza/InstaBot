#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Database.Models.BotAccount import BotAccount

class AccountManager:
    def __init__(self, uiAccountListAddSignal=None):
        self.uiAccountListAddSignal = uiAccountListAddSignal
        self.model = BotAccount()

    def fillUIAccountList(self):
        for user_row in self.model.getAllAccounts():
            self._addToUIAccountList(user_row.login, user_row.img_url)

    def _addToUIAccountList(self, name, icon):
        self.uiAccountListAddSignal.emit(name, icon)

    def getAccountByName(self, login):
        return self.model.get(BotAccount.login == login)