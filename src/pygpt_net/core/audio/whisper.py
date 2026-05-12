#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: www.dlrp.ca                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.29 18:00:00                  #
# ================================================== #

from typing import List

class Whisper:
    def __init__(self, window=None):
        """
        Whisper core

        :param window: Window instance
        """
        self.window = window
        self.voices = [
            "alloy",
            "ash",
            "ballad",
            "coral",
            "echo",
            "fable",
            "nova",
            "onyx",
            "sage",
            "shimmer",
        ]

    def get_voices(self) -> List[str]:
        """
        Get whisper voices

        :return: whisper voice name
        """
        return self.voices

