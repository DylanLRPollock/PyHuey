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

from packaging.version import parse as parse_version, Version


class Patch:
    def __init__(self, window=None, provider=None):
        self.window = window
        self.provider = provider

    def execute(self, version: Version) -> bool:
        """
        Migrate to current app version

        :param version: current app version
        :return: True if migrated
        """
        pass

