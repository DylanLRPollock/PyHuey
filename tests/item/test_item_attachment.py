#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://github.com/DylanLRPollock/PyHuey                         #
# GitHub:  https://github.com/DylanLRPollock/PyHuey   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.05 18:00:00                  #
# ================================================== #

import pygpt_net.item.attachment as attachment_mod


def test_integrity():
    """Test AttachmentItem integrity"""
    item = attachment_mod.AttachmentItem()

    assert item.name is None
    assert item.id is None
    assert item.path is None
    assert item.remote is None
    assert item.send is False

