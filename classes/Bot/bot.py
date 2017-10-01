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

        settings = self.getSettings(accountInfo)


        instaBot = InstaBot(login=accountInfo[0].login, password=accountInfo[0].password)
        instaBot.login()
        self.scheduler = Scheduler()
        self.scheduler.addTask(
            TraditionalFollowing(instaBot)
                .setDelay(45, 55)
                .setUserSource(HashTagUserSource(source=settings['userSource']['filePath']))
        )

        while self.isWorking:
            self.scheduler.start()

        print('Bot stopped.')
        self.finishBotAccountSignal.emit(accountInfo.id)

    def getSettings(self, accountInfo):
        settings = {
            'userSource': {
                'type': '',
                'filePath': '',
            },
            'like': {
                'needLike': '',
                'firstLike': '',
                'limit': '',
                'count': '',
                'range': '',
            },
            'needFollow': '',
            'isCycleLoop': '',
            'comment': {
                'needComment': '',
                'source': '',
            }
        }
        for x in accountInfo:
            if x.task.need_like:
                settings['like']['needLike'] = True
                settings['like']['firstLike'] = x.task.first_like
                settings['like']['limit'] = x.task.limit_like
                settings['like']['count'] = x.task.count_like
                settings['like']['range'] = x.task.range_like

            settings['needFollow'] = x.task.need_follow
            settings['isCycleLoop'] = x.task.is_cycleLoop

            if x.task.need_comment:
                settings['comment']['needComment'] = x.task.need_comment
                settings['comment']['source'] = x.task.comment_file_path

            if x.tasks.source_user_list_active:
                settings['userSource']['type'] = 'user_list'
                settings['userSource']['filePath'] = x.tasks.source_user_list_file_path
            if x.tasks.source_hashtag_list_active:
                settings['userSource']['type'] = 'hashTag'
                settings['userSource']['filePath'] = x.tasks.source_hashtag_list_file_path
            if x.tasks.source_geo_list_active:
                settings['userSource']['type'] = 'geo'
                settings['userSource']['filePath'] = x.tasks.source_geo_list_file_path
            if x.tasks.source_follower_list_active:
                settings['userSource']['type'] = 'followers'
                settings['userSource']['filePath'] = x.tasks.source_follower_list_file_path
            if x.tasks.source_follow_by_list_active:
                settings['userSource']['type'] = 'followedBy'
                settings['userSource']['filePath'] = x.tasks.source_follow_by_list_file_path

            return settings


    def join(self, timeout=None):
        self.isWorking = False
        print('Try stop...')