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
        XMLManager.resize(402, 92)
        self.AddTestcaseBox = QtGui.QGroupBox(XMLManager)
        self.AddTestcaseBox.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.AddTestcaseBox.setObjectName(_fromUtf8("AddTestcaseBox"))
        self.NameEdit = QtGui.QLineEdit(self.AddTestcaseBox)
        self.NameEdit.setGeometry(QtCore.QRect(70, 10, 151, 20))
        self.NameEdit.setObjectName(_fromUtf8("NameEdit"))
        self.IterationEdit = QtGui.QLineEdit(self.AddTestcaseBox)
        self.IterationEdit.setGeometry(QtCore.QRect(70, 30, 151, 20))
        self.IterationEdit.setObjectName(_fromUtf8("IterationEdit"))
        self.splitter_2 = QtGui.QSplitter(self.AddTestcaseBox)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 47, 26))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.NameLabel = QtGui.QLabel(self.splitter_2)
        self.NameLabel.setObjectName(_fromUtf8("NameLabel"))
        self.IterationLabel = QtGui.QLabel(self.splitter_2)
        self.IterationLabel.setObjectName(_fromUtf8("IterationLabel"))
        self.splitter = QtGui.QSplitter(XMLManager)
        self.splitter.setGeometry(QtCore.QRect(290, 20, 75, 46))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.OkButton = QtGui.QPushButton(self.splitter)
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.CancelButton = QtGui.QPushButton(self.splitter)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(XMLManager)
        QtCore.QObject.connect(self.CancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), XMLManager.close)
        QtCore.QMetaObject.connectSlotsByName(XMLManager)

    def retranslateUi(self, XMLManager):
        XMLManager.setWindowTitle(_translate("XMLManager", "XML Manager", None))
        self.AddTestcaseBox.setTitle(_translate("XMLManager", "Add testcase", None))
        self.NameLabel.setText(_translate("XMLManager", "Name", None))
        self.IterationLabel.setText(_translate("XMLManager", "Iterations", None))
        self.OkButton.setText(_translate("XMLManager", "OK", None))
        self.CancelButton.setText(_translate("XMLManager", "Cancel", None))

