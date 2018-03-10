#!/usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import cycle
from random import sample
from time import sleep

import inject

import DIConfig
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
        logger = inject.attr(DIConfig.Logger)

    def runTask(self, user: User):
        if not user:
            return None

        if user.isNormal():
            self.logger.log('Enter to user: {}'.format(user.username))
            self.logger.log('User link: https://www.instagram.com/{}/'.format(user.username))

            if not user.isFollower:
                if self.getLikeSettings()['needLike']:
                    likeList = self.getLikeFromLastMedia(
                        user,
                        self.getLikeSettings()['count'],
                        self.getLikeSettings()['range'],
                        like_first=self.getLikeSettings()['firstLike']
                    )
                    for mediaId in likeList:
                        self._insta.like(mediaId)
                        sleep(7)

                if self.needFollow():
                    self._insta.follow(user.id)

                if self.needComment():
                    self._insta.comment(
                        user.media[0]['id'],
                        self.getCommentGenerator().generate()
                    )

            self.setNextExec()
        else:
            self.logger.log('Skip user #%d: %s' % (self.userIndex - 1, user.username))
            self.logger.log('User link: ' + "https://www.instagram.com/%s/" % user.username)

        self.logger.log('\n')

    def getLikeFromLastMedia(self, currentUser: User, likeCount, lastMediaRange, like_first=False):
        countMedia = len(currentUser.media)
        if likeCount > countMedia or likeCount > lastMediaRange:
            likeCount = min((countMedia, lastMediaRange))
        if countMedia < lastMediaRange:
            lastMediaRange = countMedia
        likeListId = []
        minLikeMediaNumber = 1
        if like_first:
            likeListId.append(currentUser.media[minLikeMediaNumber]['id'])
            minLikeMediaNumber += 1
        if (lastMediaRange - minLikeMediaNumber) < likeCount:
            likeCount = lastMediaRange - minLikeMediaNumber
        if lastMediaRange == 1 and not like_first:
            likeListId.append(currentUser.media[1]['id'])
        else:
            for number in sample(range(minLikeMediaNumber, lastMediaRange), likeCount):
                likeListId.append(currentUser.media[number]['id'])
        return likeListId