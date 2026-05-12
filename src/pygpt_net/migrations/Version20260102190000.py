#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2026.01.02 20:00:00                  #
# ================================================== #

from sqlalchemy import text

from .base import BaseMigration


class Version20260102190000(BaseMigration):
    def __init__(self, window=None):
        super(Version20260102190000, self).__init__(window)
        self.window = window

    def up(self, conn):
        conn.execute(text("""
        ALTER TABLE remote_store ADD COLUMN provider TEXT;
        """))
        conn.execute(text("""
        ALTER TABLE remote_file ADD COLUMN provider TEXT;
        """))
        # set all to OpenAI by default
        conn.execute(text("""
        UPDATE remote_store SET provider = 'openai' WHERE provider IS NULL;
        """))
        conn.execute(text("""
        UPDATE remote_file SET provider = 'openai' WHERE provider IS NULL;
        """))

