#!/usr/bin/python3
# -*- coding: utf-8 -*-
from threading import Thread
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from classes.Bot.Scheduler import Scheduler
from classes.Database.Models.Accounts import Accounts
from classes.Database.Models.TaskSettings import Tasks
from classes.Instagram.InstaBot import InstaBot
from classes.Instagram.instaUser import User
from classes.Tasks.FollowAndUnfollow import FollowAndUnfollow
from classes.Tasks.TraditionalFollowing import TraditionalFollowing
from classes.TextGenerator.MsgGenerator import MsgGenerator
from classes.UserSource.UserSourceContainer import UserSourceContainer
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

        userSource = UserSourceContainer().getUserSource(settings['userSource']['type'])
        userSource = userSource(settings['userSource']['filePath'])
        userSource.isCycle(settings['isCycleLoop'])

        instaBot = InstaBot(login=accountInfo[0].login, password=accountInfo[0].password)
        instaBot.login()
        self.scheduler = Scheduler()
        self.scheduler.addTask(
            TraditionalFollowing(instaBot)
                .setDelay(45, 55)
                .setUserSource(userSource)
                .setLikeSettings(settings['like'])
                .needFollow(settings['needFollow'])
                .needComment(settings['comment']['needComment'])
                .setCommentGenerator(MsgGenerator(settings['comment']['source'], type=MsgGenerator.TYPE_FILE))
        )

        while self.isWorking:
            self.scheduler.start()

        print('Bot stopped.')
        self.finishBotAccountSignal.emit(accountInfo[0].id)

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
            if x.tasks.need_like:
                settings['like']['needLike'] = True
                settings['like']['firstLike'] = x.tasks.first_like
                settings['like']['limit'] = x.tasks.limit_like
                settings['like']['count'] = x.tasks.count_like
                settings['like']['range'] = x.tasks.range_like

            settings['needFollow'] = x.tasks.need_follow
            settings['isCycleLoop'] = x.tasks.is_cycleLoop

            if x.tasks.need_comment:
                settings['comment']['needComment'] = x.tasks.need_comment
                settings['comment']['source'] = x.tasks.comment_file_path

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