# Copyright (C) 2026 Qt Group.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o7_Text))
    mouseClick(waitForObject(names.o8_Text))
    mouseClick(waitForObject(names.o9_Text))
    test.vp("VP1")
