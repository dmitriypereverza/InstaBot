#!/usr/bin/python3
# -*- coding: utf-8 -*-
from threading import Thread

from classes.Bot.Scheduler import Scheduler
from classes.Database.Models.Accounts import Accounts
from classes.Database.Models.TaskSettings import Tasks
from classes.Instagram.InstaBot import InstaBot
from classes.Instagram.instaUser import User
from classes.Tasks.FollowAndUnfollow import FollowAndUnfollow
from classes.Tasks.TraditionalFollowing import TraditionalFollowing
from classes.UserSource.UserSources import HashTagUserSource

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
        accountInfo = (Accounts \
                       .select(Accounts, Tasks) \
                       .join(Tasks) \
                       .where(Accounts.login == self.account_login))

        userSource = {
            'type': '',
            'filePath': '',
        }
        for x in accountInfo:
            if x.tasks.source_user_list_active:
                userSource['type'] = 'user_list'
                userSource['filePath'] = x.tasks.source_user_list_file_path
            if x.tasks.source_hashtag_list_active:
                userSource['type'] = 'hashTag'
                userSource['filePath'] = x.tasks.source_hashtag_list_file_path
            if x.tasks.source_geo_list_active:
                userSource['type'] = 'geo'
                userSource['filePath'] = x.tasks.source_geo_list_file_path
            if x.tasks.source_follower_list_active:
                userSource['type'] = 'followers'
                userSource['filePath'] = x.tasks.source_follower_list_file_path
            if x.tasks.source_follow_by_list_active:
                userSource['type'] = 'followedBy'
                userSource['filePath'] = x.tasks.source_follow_by_list_file_path


        instaBot = InstaBot(login=accountInfo[0].login, password=accountInfo[0].password)
        instaBot.login()
        self.scheduler = Scheduler()
        self.scheduler.addTask(
            TraditionalFollowing(instaBot)
                .setDelay(45, 55)
                .setUserSource(HashTagUserSource(source=userSource['filePath']))
        )

        while self.isWorking:
            self.scheduler.start()

        print('Bot stopped.')
        self.finishBotAccountSignal.emit(accountInfo.id)


    def join(self, timeout=None):
        self.isWorking = False
        print('Try stop...')