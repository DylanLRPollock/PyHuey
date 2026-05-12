#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.27 14:00:00                  #
# ================================================== #

class BaseMigration:
    def __init__(self, window=None):
        self.window = window

    def up(self, conn):
        pass

