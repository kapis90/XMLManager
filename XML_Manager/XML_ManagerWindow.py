# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documenty\Projects\python\XML_Manager\XML_Manager\XML_Manager\XML_ManagerWindow.ui'
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
        XMLManager.resize(671, 440)
        self.AddTestcaseBox = QtGui.QGroupBox(XMLManager)
        self.AddTestcaseBox.setGeometry(QtCore.QRect(10, 55, 656, 326))
        self.AddTestcaseBox.setObjectName(_fromUtf8("AddTestcaseBox"))
        self.tableWidget = QtGui.QTableWidget(self.AddTestcaseBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 250, 300))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.BrowseBox = QtGui.QGroupBox(XMLManager)
        self.BrowseBox.setGeometry(QtCore.QRect(5, 5, 661, 51))
        self.BrowseBox.setObjectName(_fromUtf8("BrowseBox"))
        self.XMLPathEdit = QtGui.QLineEdit(self.BrowseBox)
        self.XMLPathEdit.setGeometry(QtCore.QRect(10, 20, 561, 20))
        self.XMLPathEdit.setObjectName(_fromUtf8("XMLPathEdit"))
        self.BrowseButton = QtGui.QPushButton(self.BrowseBox)
        self.BrowseButton.setGeometry(QtCore.QRect(580, 18, 75, 23))
        self.BrowseButton.setObjectName(_fromUtf8("BrowseButton"))
        self.ApplyButton = QtGui.QPushButton(XMLManager)
        self.ApplyButton.setGeometry(QtCore.QRect(586, 395, 75, 23))
        self.ApplyButton.setObjectName(_fromUtf8("ApplyButton"))
        self.buttonGroup = QtGui.QButtonGroup(XMLManager)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.ApplyButton)
        self.CancelButton = QtGui.QPushButton(XMLManager)
        self.CancelButton.setGeometry(QtCore.QRect(505, 395, 75, 23))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.buttonGroup.addButton(self.CancelButton)
        self.OkButton = QtGui.QPushButton(XMLManager)
        self.OkButton.setGeometry(QtCore.QRect(425, 395, 75, 23))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.buttonGroup.addButton(self.OkButton)

        self.retranslateUi(XMLManager)
        QtCore.QMetaObject.connectSlotsByName(XMLManager)
        XMLManager.setTabOrder(self.XMLPathEdit, self.BrowseButton)
        XMLManager.setTabOrder(self.BrowseButton, self.tableWidget)
        XMLManager.setTabOrder(self.tableWidget, self.OkButton)
        XMLManager.setTabOrder(self.OkButton, self.CancelButton)
        XMLManager.setTabOrder(self.CancelButton, self.ApplyButton)

    def retranslateUi(self, XMLManager):
        XMLManager.setWindowTitle(_translate("XMLManager", "XML Manager", None))
        self.AddTestcaseBox.setTitle(_translate("XMLManager", "Manage benchmarks", None))
        self.BrowseBox.setTitle(_translate("XMLManager", "Browse for XML File:", None))
        self.BrowseButton.setText(_translate("XMLManager", "Browse", None))
        self.ApplyButton.setText(_translate("XMLManager", "Apply", None))
        self.CancelButton.setText(_translate("XMLManager", "Cancel", None))
        self.OkButton.setText(_translate("XMLManager", "OK", None))

