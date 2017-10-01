#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from random import sample
from time import sleep

from classes.Instagram.instaUser import User
from classes.Log.Log import Logger
from classes.Source.commentTemplateList import templateListEn
from classes.Tasks.BaseTask import BaseTask
from classes.TextGenerator.MsgGenerator import MsgGenerator

class TraditionalFollowing(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.userIndex = 0
        self.tagsGenerator = None

    def runTask(self, user: User):
        if not user:
            return None

        if user.isNormal():
            Logger().log('Enter to user: {}'.format(user.username))
            Logger().log('User link: https://www.instagram.com/{}/'.format(user.username))

            if not user.isFollower:
                likeList = self.getLikeFromLastMedia(user, 1, 1)
                for mediaId in likeList:
                    self._insta.like(mediaId)
                    sleep(7)

                # self.insta.follow(currentUser.id)
                self.writeComment(user)

            self.setNextExec()
        else:
            Logger().log('Skip user #%d: %s' % (self.userIndex - 1, user.username))
            Logger().log('User link: ' + "https://www.instagram.com/%s/" % user.username)

        Logger().log('\n')

    def writeComment(self, currentUser: User):
        comment = MsgGenerator(templateListEn).generate()
        self._insta.comment(currentUser.media[0]['id'], comment)

    def getLikeFromLastMedia(self, currentUser: User, lastMediaRange, likeCount):
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