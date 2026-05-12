#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2026.01.21 13:00:00                  #
# ================================================== #

from .anthropic import ApiAnthropic
from .google import ApiGoogle
from .openai import ApiOpenAI
from .x_ai import ApiXAI

class Api:

    def __init__(self, window=None):
        """
        API wrappers

        :param window: Window instance
        """
        self.window = window
        self.anthropic = ApiAnthropic(window)
        self.google = ApiGoogle(window)
        self.openai = ApiOpenAI(window)
        self.xai = ApiXAI(window)

    def stop(self):
        """Stop all API clients"""
        self.anthropic.stop()
        self.google.stop()
        self.openai.stop()
        self.xai.stop()

    def close(self):
        """Close all API clients"""
        self.anthropic.safe_close()
        self.google.safe_close()
        self.openai.safe_close()
        self.xai.safe_close()
