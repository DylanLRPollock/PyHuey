#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: www.dlrp.ca                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2026.01.21 20:00:00                  #
# ================================================== #

from sqlalchemy import text

from .base import BaseMigration


class Version20260121190000(BaseMigration):
    def __init__(self, window=None):
        super(Version20260121190000, self).__init__(window)
        self.window = window

    def up(self, conn):
        conn.execute(text("""
        ALTER TABLE notepad ADD COLUMN highlights_json TEXT;
        """))


