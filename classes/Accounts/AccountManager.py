#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Database.Models.Accounts import Accounts

class AccountManager:
    def __init__(self, uiAccountListAddSignal=None):
        self.uiAccountListAddSignal = uiAccountListAddSignal
        self.model = Accounts()

    def fillUIAccountList(self):
        for user_row in self.model.getAllAccounts():
            self._addToUIAccountList(user_row.login, user_row.img_url, user_row.id)

    def _addToUIAccountList(self, name, icon, id):
        self.uiAccountListAddSignal.emit(name, icon, id)

    def getAccountByName(self, login):
        return self.model.get(Accounts.login == login)