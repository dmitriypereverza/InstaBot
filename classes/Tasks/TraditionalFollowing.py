#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from random import sample
from time import sleep

from classes.Instagram.instaUser import User
from classes.Log.LogClass import Logger
from classes.Sourse.commentTemplateList import templateListEn
from classes.Tasks.BaseTask import BaseTask
from classes.TextGenerator.MsgGenerator import MsgGenerator

class TraditionalFollowing(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.userIndex = 0
        self.tagsGenerator = None

    def runTask(self):
        if not self._usersList:
            # self.usersList = self.getUsersByLocation(225196070)
            # self.usersList = self.getUsersFollowers('fudduxujd')
            self._usersList = self.getUsersByTag(self.getNextTag())

        currentUser = self.getNextUser()
        if not currentUser:
            return None

        if currentUser.isNormal():
            Logger.log('Enter to user #{}: {}'.format(self.userIndex - 1, currentUser.username))
            Logger.log('User link: https://www.instagram.com/{}/'.format(currentUser.username))

            if not currentUser.isFollower:
                likeList = self.getLikeFromLastMedia(currentUser, 1, 1)
                for mediaId in likeList:
                    self._insta.like(mediaId)
                    sleep(7)

                # self.insta.follow(currentUser.id)
                self.writeComment(currentUser)

            self.setNextExec()
        else:
            Logger.log('Skip user #%d: %s' % (self.userIndex - 1, currentUser.username))
            Logger.log('User link: ' + "https://www.instagram.com/%s/" % currentUser.username)

        Logger.log('\n')

    def writeComment(self, currentUser):
        comment = MsgGenerator(templateListEn).generate()
        self._insta.comment(currentUser.media[0]['id'], comment)

    def getLikeFromLastMedia(self, currentUser, lastMediaRange, likeCount):
        countMedia = len(currentUser.media)
        if likeCount > countMedia or likeCount > lastMediaRange:
            likeCount = min((countMedia, lastMediaRange))
        if countMedia < lastMediaRange:
            lastMediaRange = countMedia
        likeListId = []
        if lastMediaRange == 1:
            likeListId.append(currentUser.media[1]['id'])
        else:
            for number in sample(range(1, lastMediaRange), likeCount):
                likeListId.append(currentUser.media[number]['id'])
        return likeListId

    def getNextTag(self):
        self.tagsGenerator = cycle(self._tagsList) if not self.tagsGenerator else self.tagsGenerator
        return next(self.tagsGenerator)

    def getNextUser(self) -> User:
        return self._usersList.pop()

    def getUsersByTag(self, tag):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUserNamesByTag(tag)
        ))

    def getUsersFollowers(self, username):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUserFollowers(username, 50)
        ))

    def getUsersByLocation(self, locationId):
        return list(map(
            lambda x: User(self._insta.getUserInfoByLogin(x)),
            self._insta.getUsersByLocation(locationId)
        ))