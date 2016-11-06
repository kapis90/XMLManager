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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(402, 92)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 30, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.splitter_2 = QtGui.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(10, 20, 47, 26))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label = QtGui.QLabel(self.splitter_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(290, 20, 75, 46))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pushButton = QtGui.QPushButton(self.splitter)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "XML Manager", None))
        self.groupBox.setTitle(_translate("Form", "Add testcase", None))
        self.label.setText(_translate("Form", "Name", None))
        self.label_2.setText(_translate("Form", "Iterations", None))
        self.pushButton.setText(_translate("Form", "OK", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))

