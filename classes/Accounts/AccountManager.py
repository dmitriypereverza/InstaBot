#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.Database.Models.BotAccount import BotAccount

class AccountManager:
    def __init__(self, uiAccountListAddSignal):
        self.uiAccountListAddSignal = uiAccountListAddSignal
        self.model = BotAccount()

    def fillUIAccountList(self):
        for user_row in self.model.getAllAccounts():
            self.addToUIAccountList(user_row.login,  user_row.img_url)

    def addToUIAccountList(self, name, icon):
        self.uiAccountListAddSignal.emit(name, icon)