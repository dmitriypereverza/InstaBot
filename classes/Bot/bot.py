#!/usr/bin/python3
# -*- coding: utf-8 -*-
from threading import Thread

from classes.Bot.Scheduler import Scheduler
from classes.Database.Models.Accounts import Accounts
from classes.Instagram.InstaBot import InstaBot
from classes.Instagram.instaUser import User
from classes.Tasks.FollowAndUnfollow import FollowAndUnfollow
from classes.Tasks.TraditionalFollowing import TraditionalFollowing

class AccountThread(Thread):
    def __init__(self, login, finishBotAccountSignal):
        Thread.__init__(self)
        self.finishBotAccountSignal = finishBotAccountSignal
        self.isWorking = True
        self.daemon = True
        self.account_login = login
        self.name = login
        self.scheduler = Scheduler()

    def run(self):
        accountInfo = Accounts.get(Accounts.login == self.account_login)

        instaBot = InstaBot(login=accountInfo.login, password=accountInfo.password)
        instaBot.login()
        self.setScheduler(instaBot)

        while self.isWorking:
            self.scheduler.start()

        print('Bot stopped.')
        self.finishBotAccountSignal.emit(accountInfo.id)

    def setScheduler(self, instaBot):
        self.scheduler = Scheduler()
        self.scheduler.addTask(
            TraditionalFollowing(instaBot)
                .setDelay(45, 55)
                .setTagsList(['mobilephoto', 'draw', 'artwork'])
                .showTime()
        )
        self.scheduler.addTask(
            FollowAndUnfollow(instaBot)
                .setDelay(50, 60)
                .setUsersList([User(instaBot.getUserInfoByLogin('timatiofficial'))])
        )

    def join(self, timeout=None):
        self.isWorking = False
        print('Try stop...')