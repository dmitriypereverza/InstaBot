#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.Tasks.BaseTask import BaseTask

class AddFriend(BaseTask):
    def __init__(self, insta):
        super().__init__(insta)
        self.delay = [35, 55]

    def runTask(self):
        currentUser = self.users_list[self.currentIndex]
        """:type currentUser: User"""
        if currentUser.isFollowing:
            self.insta.unfollow(currentUser.id)
        else:
            self.insta.follow(currentUser.id)

        self.users_list[self.currentIndex].isFollowing = not currentUser.isFollowing
        self.currentIndex = (self.currentIndex + 1) % len(self.users_list)
        self.setNextExec()