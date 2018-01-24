#! /usr/bin/python

import os
import sys




from PySide import QtGui, QtCore
# we need to import the QUiLoader as well for this
# I'm just messing with this file on purpose to prove a point
from PySide.QtUiTools import QUiLoader
from functools import partial

# this is the path the to .ui file that we've created
PATH_TO_UI_FILE = "/Users/stauffer/Documents/Development/PycharmProjects/SimpleMath/simpleMathGui.ui"

def createInterface():

    # create a new instance of the loader
    loader = QUiLoader()

    # Load up the file into a QFile Object
    q_file = QtCore.QFile(PATH_TO_UI_FILE)
    q_file.open(QtCore.QFile.ReadOnly)

    # use the loader to load the widget from the file
    widget = loader.load(q_file, None)



    # you can access the child widgets from the UI file as regular variables
    # the name will match the name of the widgets given inside Designer
    widget.pushButton.clicked.connect(partial(do_something,widget.doubleSpinBox))

    #widget.plainTextEdit.textChanged.connect(now_this)


    # close the file
    q_file.close()

    # return the widget to Houdini
    return widget



def do_something(x):
    print "Connected the signal from inside the UI File! "
    print
    value = int(x.cleanText())
    res = value * 10
    print res



