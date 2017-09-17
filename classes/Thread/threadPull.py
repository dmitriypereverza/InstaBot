#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading

from classes.DecoHelpers.classDecorators import singleton

@singleton
class ThreadsPull:
    max_threads = 20
    max_connections = 5
    queue = threading.BoundedSemaphore(value=max_connections)

    def startOrStopThread(self, thread):
        searchedThread = self.getByName(thread.account_login)
        if not searchedThread:
            thread.start()
        elif not searchedThread.is_alive():
            thread.start()
        else:
            searchedThread.join()

    def getByName(self, name) -> threading.Thread:
         for thread in threading.enumerate():
             if thread.name == name:
                 return thread