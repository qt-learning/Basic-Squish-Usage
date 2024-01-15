# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o3_Text))
    mouseClick(waitForObject(names.o2_Text))
    mouseClick(waitForObject(names.o1_Text))
    test.imagePresent("image")
