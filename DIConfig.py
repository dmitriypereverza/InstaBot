#!/usr/bin/python3
# -*- coding: utf-8 -*-

import inject
from classes.Log.Log import Logger as LoggerConfig
from classes.Log.Loggers.ConsoleLogger import ConsoleLogger

class Logger: pass

def my_config(binder):
    binder.bind(
        Logger,
        LoggerConfig().setLoggerType(ConsoleLogger())
    )

inject.configure_once(my_config)