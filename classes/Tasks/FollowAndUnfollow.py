#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class FollowAndUnfollow(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]

    def runTask(self):
        currentUser = self.usersList[self.currentIndex]
        """:type currentUser: User"""
        if currentUser.isFollowing:
            self.insta.unfollow(currentUser.id)
        else:
            self.insta.follow(currentUser.id)

        self.usersList[self.currentIndex].isFollowing = not currentUser.isFollowing
        self.currentIndex = (self.currentIndex + 1) % len(self.usersList)
        self.setNextExec()