# Copyright (C) 2026 Qt Group.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o3_Text))
    mouseClick(waitForObject(names.o2_Text))
    mouseClick(waitForObject(names.o1_Text))
    test.imagePresent("image")
