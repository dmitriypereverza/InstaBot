#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from random import sample
from time import sleep

from classes.Instagram.userinfo import User
from classes.Log.LogClass import Logger
from classes.Sourse.commentTemplateList import templateList
from classes.Tasks.BaseTask import BaseTask
from classes.TextGenerator.MsgGenerator import MsgGenerator

class TraditionalFollowing(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]
        self.tagIndex = 0
        self.userIndex = 0
        self.tagPostIndex = 0
        self.tagsGenerator = None

    def runTask(self):
        if not self.usersList:
            # self.usersList = self.getUsersByLocation(225196070)
            # self.usersList = self.getUsersFollowers('fudduxujd')
            self.usersList = self.getUsersByTag(self.getNextTag())

        currentUser = self.getNextUser()
        if not currentUser:
            return None

        if currentUser.isNormal():
            Logger.log('Enter to user #%d: %s' % (self.userIndex - 1, currentUser.username))
            Logger.log('User link: ' + "https://www.instagram.com/%s/" % currentUser.username)
            likeList = self.getLikeListId(currentUser)
            for mediaId in likeList:
                self.insta.like(mediaId)
                sleep(7)

            if not currentUser.isFollower:
                self.insta.follow(currentUser.id)
                self.writeComment(currentUser)

            self.setNextExec()
        else:
            Logger.log('Skip user #%d: %s' % (self.userIndex - 1, currentUser.username))
            Logger.log('User link: ' + "https://www.instagram.com/%s/" % currentUser.username)

        Logger.log('\n')

    def writeComment(self, currentUser):
        comment = MsgGenerator(templateList).generate()
        Logger.log('Comment: %s' % comment)
        self.insta.comment(currentUser.media[0]['id'], comment)

    def getLikeListId(self, currentUser):
        countMedia = len(currentUser.media)
        likeListId = []
        if 0 < countMedia <= 3:
            for media in currentUser.media:
                likeListId.append(media['id'])
        if 3 < countMedia < 10:
            likeListId.append(currentUser.media[0]['id'])
            for number in sample(range(1, countMedia), 2):
                likeListId.append(currentUser.media[number]['id'])
        if countMedia >= 10:
            likeListId.append(currentUser.media[0]['id'])
            for number in sample(range(1, 10), 2):
                likeListId.append(currentUser.media[number]['id'])

        return likeListId

    def getNextTag(self):
        self.tagsGenerator = cycle(self.tagsList) if not self.tagsGenerator else self.tagsGenerator
        return next(self.tagsGenerator)

    def getNextUser(self) -> User:
        userNext = None
        if len(self.usersList) > self.userIndex:
            userNext = self.usersList[self.userIndex]
            self.userIndex += 1
        else:
            self.usersList = []
            self.userIndex = 0
        return userNext

    def getUsersByTag(self, tag):
        return list(map(
            lambda x: User.getUserByName(x),
            self.insta.getUserNamesByTag(tag)
        ))

    def getUsersFollowers(self, username):
        return list(map(
            lambda x: User.getUserByName(x),
            self.insta.getUserFollowers(username, 50)
        ))

    def getUsersByLocation(self, locationId):
        return list(map(
            lambda x: User.getUserByName(x),
            self.insta.getUsersByLocation(locationId)
        ))