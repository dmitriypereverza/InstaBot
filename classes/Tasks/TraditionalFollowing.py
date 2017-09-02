#!/usr/bin/python3
# -*- coding: utf-8 -*-
from random import sample
from time import sleep

from classes.Instagram.userSearcher import UserSearcher
from classes.Instagram.userinfo import User
from classes.Log.LogClass import Logger
from classes.Tasks.BaseTask import BaseTask


class TraditionalFollowing(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]
        self.tagIndex = 0
        self.userIndex = 0
        self.tagPostIndex = 0

    def runTask(self):
        if not self.usersList:
            nextTag = self.getNextTag()
            self.usersList = self.getUsersByTag(nextTag)
            Logger.log('Count user by tag ' + nextTag + ': ' + str(len(self.usersList)))

        currentUser = self.getNextUser()
        if not currentUser:
            return None

        if not currentUser.isFollower and currentUser.isNormal():
            Logger.log('Enter to user #%d: %s' % (self.userIndex - 1, currentUser.username))
            Logger.log('User link: ' + "https://www.instagram.com/%s/" % currentUser.username)
            for mediaId in self.getLikeListId(currentUser):
                self.insta.like(mediaId)
                sleep(7)

            self.insta.follow(currentUser.id)
            self.setNextExec()
        else:
            Logger.log('Skip user #%d: %s' % (self.userIndex - 1, currentUser.username))
            Logger.log('User link: ' + "https://www.instagram.com/%s/" % currentUser.username)

        Logger.log('\n')

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
        if len(self.tagsList) - 1 < self.tagIndex:
            self.tagIndex = 0

        tagNext = self.tagsList[self.tagIndex]
        self.tagIndex += 1
        return tagNext

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
            lambda x: self.insta.getUserBylogin(x),
            UserSearcher(self.insta).getUserNamesByTag(tag)
        ))