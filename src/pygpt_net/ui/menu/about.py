#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# PyHuey cockpit About menu                          #
# Website: https://www.dlrp.ca                       #
# GitHub:  https://github.com/DylanLRPollock/PyHuey  #
# Upstream: https://github.com/szczyglis-dev/py-gpt  #
# ================================================== #

from PySide6.QtGui import QAction, QIcon


class About:
    def __init__(self, window=None):
        """
        Minimal PyHuey About menu.

        Keeps the top-level About dropdown available for provenance/contact
        without exposing upstream package stores, donation links, changelog,
        updater, Discord, docs, PyPI, Snap, Microsoft Store, or legacy dialogs.
        """
        self.window = window

    def setup(self):
        """Setup minimal PyHuey About menu."""
        w = self.window
        m = w.ui.menu

        icon_public = QIcon(":/icons/public_filled.svg")

        m["info.website"] = QAction(icon_public, "dlrp.ca", w)
        m["info.github"] = QAction(icon_public, "GitHub", w)

        dlg_info = w.controller.dialogs.info

        m["info.website"].triggered.connect(
            lambda checked=False, i=dlg_info: i.goto_website()
        )
        m["info.github"].triggered.connect(
            lambda checked=False, i=dlg_info: i.goto_github()
        )

        m["menu.about"] = w.menuBar().addMenu("About")
        m["menu.about"].addActions([
            m["info.website"],
            m["info.github"],
        ])
