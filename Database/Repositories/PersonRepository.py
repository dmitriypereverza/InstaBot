#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Database.Models.Person import Person


class PersonRepository(Person):
    def __init__(self):
        super().__init__()
