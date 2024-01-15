# encoding: UTF-8

from objectmaphelper import *

#calqlatr names
o_QQuickView = {"type": "QQuickView", "unnamed": 1, "visible": True}
o7_Text = {"container": o_QQuickView, "text": 7, "type": "Text", "unnamed": 1, "visible": True}
o_Text = {"container": o_QQuickView, "text": "×", "type": "Text", "unnamed": 1, "visible": True}
o8_Text = {"container": o_QQuickView, "text": 8, "type": "Text", "unnamed": 1, "visible": True}
o_Text_2 = {"container": o_QQuickView, "text": "=", "type": "Text", "unnamed": 1, "visible": True}
listView_ListView = {"container": o_QQuickView, "id": "listView", "type": "ListView", "unnamed": 1, "visible": True}
listView_Item = {"container": listView_ListView, "index": 2, "type": "Item", "unnamed": 1, "visible": True}
o56_Text = {"container": listView_Item, "text": 56, "type": "Text", "unnamed": 1, "visible": True}
o_Text_3 = {"container": o_QQuickView, "text": "+", "type": "Text", "unnamed": 1, "visible": True}
o2_Text = {"container": o_QQuickView, "text": 2, "type": "Text", "unnamed": 1, "visible": True}
window_Rectangle = {"container": o_QQuickView, "id": "window", "type": "Rectangle", "unnamed": 1, "visible": True}
o9_Text = {"container": o_QQuickView, "text": 9, "type": "Text", "unnamed": 1, "visible": True}
o3_Text = {"container": o_QQuickView, "text": 3, "type": "Text", "unnamed": 1, "visible": True}
o1_Text = {"container": o_QQuickView, "text": 1, "type": "Text", "unnamed": 1, "visible": True}

#addressbook names
address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book"}
address_Book_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Unnamed"}
address_Book_Unnamed_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Cancel_QPushButton = {"text": "Cancel", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow, "windowTitle": "File"}
address_Book_Unnamed_File_QTableWidget = {"aboveWidget": address_Book_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_Unnamed_MainWindow}
