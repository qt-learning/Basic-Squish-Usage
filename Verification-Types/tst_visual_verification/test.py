# Copyright (C) 2026 Qt Group.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o7_Text))
    mouseClick(waitForObject(names.o8_Text))
    mouseClick(waitForObject(names.o9_Text))
    test.vp("VP1")
