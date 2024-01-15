# -*- coding: utf-8 -*-

import names


def main():
    startApplication("addressbook")
    clickButton(waitForObject(names.address_Book_New_QToolButton))
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "John")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Doe")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "John.Doe@email.com")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "111-222-3333")
    type(waitForObject(names.phone_LineEdit), "<Return>")
    clickButton(waitForObject(names.address_Book_Unnamed_Add_QToolButton))
    type(waitForObject(names.forename_LineEdit), "Jane")
    type(waitForObject(names.forename_LineEdit), "<Tab>")
    type(waitForObject(names.surname_LineEdit), "Doe")
    type(waitForObject(names.surname_LineEdit), "<Tab>")
    type(waitForObject(names.email_LineEdit), "Jane.Doe@email.com")
    type(waitForObject(names.email_LineEdit), "<Tab>")
    type(waitForObject(names.phone_LineEdit), "444-555-6666")
    type(waitForObject(names.phone_LineEdit), "<Return>")
    test.vp("VP1")
