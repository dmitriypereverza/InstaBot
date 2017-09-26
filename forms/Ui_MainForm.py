# -*- coding: utf-8 -*-
from PyQt5 import uic

MainBase, MainForm = uic.loadUiType('/home/west920/PycharmProjects/InstaBot/forms/ui/startForm.ui')
class Ui_MainForm(MainBase, MainForm):

    def __init__(self, parent=None):
        super(MainBase, self).__init__(parent)
