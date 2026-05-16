#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# PyHuey cockpit launcher                            #
# Website: https://www.dlrp.ca                       #
# GitHub:  https://github.com/DylanLRPollock/PyHuey  #
# Upstream: https://github.com/szczyglis-dev/py-gpt  #
# ================================================== #

import sys
from pathlib import Path

sys.path.insert(0, str((Path(__file__).parent / "src").resolve()))

from pygpt_net.license_gate import ensure_license_acceptance
from pygpt_net.app import run

if __name__ == "__main__":
    ensure_license_acceptance()
    run()
