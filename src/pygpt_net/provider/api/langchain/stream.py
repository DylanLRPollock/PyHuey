#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2026.01.05 20:00:00                  #
# ================================================== #

from typing import Optional


def process_langchain_chat(chunk) -> Optional[str]:
    """
    LangChain chat streaming delta.

    :param chunk: Incoming streaming chunk
    :return: Extracted text delta or None
    """
    if getattr(chunk, "content", None) is not None:
        return str(chunk.content)
    return None
