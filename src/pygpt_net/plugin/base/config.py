#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: www.dlrp.ca                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.12.14 00:00:00                  #
# ================================================== #

from typing import Optional

from .plugin import BasePlugin

class BaseConfig:
    def __init__(self, plugin: BasePlugin = None, *args, **kwargs):
        self.plugin = plugin

    def from_defaults(self, plugin: Optional[BasePlugin] = None):
        """
        Set default options for plugin

        :param plugin: plugin instance
        """
        pass


