# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XML_ManagerWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_XMLManager(object):
    def setupUi(self, XMLManager):
        XMLManager.setObjectName(_fromUtf8("XMLManager"))
        XMLManager.resize(392, 220)
        self.AddTestcaseBox = QtGui.QGroupBox(XMLManager)
        self.AddTestcaseBox.setGeometry(QtCore.QRect(10, 80, 281, 71))
        self.AddTestcaseBox.setObjectName(_fromUtf8("AddTestcaseBox"))
        self.NameEdit = QtGui.QLineEdit(self.AddTestcaseBox)
        self.NameEdit.setGeometry(QtCore.QRect(80, 20, 151, 20))
        self.NameEdit.setObjectName(_fromUtf8("NameEdit"))
        self.IterationEdit = QtGui.QLineEdit(self.AddTestcaseBox)
        self.IterationEdit.setGeometry(QtCore.QRect(80, 40, 151, 20))
        self.IterationEdit.setObjectName(_fromUtf8("IterationEdit"))
        self.NameLabel = QtGui.QLabel(self.AddTestcaseBox)
        self.NameLabel.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.NameLabel.setObjectName(_fromUtf8("NameLabel"))
        self.IterationLabel = QtGui.QLabel(self.AddTestcaseBox)
        self.IterationLabel.setGeometry(QtCore.QRect(20, 40, 47, 16))
        self.IterationLabel.setObjectName(_fromUtf8("IterationLabel"))
        self.BrowseBox = QtGui.QGroupBox(XMLManager)
        self.BrowseBox.setGeometry(QtCore.QRect(10, 10, 371, 51))
        self.BrowseBox.setObjectName(_fromUtf8("BrowseBox"))
        self.XMLPathEdit = QtGui.QLineEdit(self.BrowseBox)
        self.XMLPathEdit.setGeometry(QtCore.QRect(11, 22, 271, 20))
        self.XMLPathEdit.setObjectName(_fromUtf8("XMLPathEdit"))
        self.BrowseButton = QtGui.QPushButton(self.BrowseBox)
        self.BrowseButton.setGeometry(QtCore.QRect(285, 21, 75, 23))
        self.BrowseButton.setObjectName(_fromUtf8("BrowseButton"))
        self.CancelButton = QtGui.QPushButton(XMLManager)
        self.CancelButton.setGeometry(QtCore.QRect(202, 171, 75, 23))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.OkButton = QtGui.QPushButton(XMLManager)
        self.OkButton.setGeometry(QtCore.QRect(121, 171, 75, 23))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))

        self.retranslateUi(XMLManager)
        QtCore.QObject.connect(self.CancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), XMLManager.close)
        QtCore.QMetaObject.connectSlotsByName(XMLManager)

    def retranslateUi(self, XMLManager):
        XMLManager.setWindowTitle(_translate("XMLManager", "XML Manager", None))
        self.AddTestcaseBox.setTitle(_translate("XMLManager", "Add testcase", None))
        self.NameLabel.setText(_translate("XMLManager", "Name", None))
        self.IterationLabel.setText(_translate("XMLManager", "Iterations", None))
        self.BrowseBox.setTitle(_translate("XMLManager", "Browse for XML File:", None))
        self.BrowseButton.setText(_translate("XMLManager", "Browse", None))
        self.CancelButton.setText(_translate("XMLManager", "Cancel", None))
        self.OkButton.setText(_translate("XMLManager", "OK", None))

