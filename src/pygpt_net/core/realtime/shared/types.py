#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.31 23:00:00                  #
# ================================================== #

from typing import Optional, Callable, Awaitable

TextCallback = Callable[[str], Awaitable[None]]
AudioCallback = Callable[[bytes, str, Optional[int], Optional[int], bool], Awaitable[None]]
StopCallback = Callable[[], bool]
