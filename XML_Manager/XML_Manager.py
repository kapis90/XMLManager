import sys 
from PyQt4 import QtCore, QtGui
from XML_ManagerWindow import Ui_XMLManager

class XMLManager(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_XMLManager()
        self.ui.setupUi(self)
        self.ui.OkButton.clicked.connect(self.CopyEntry)
        self.ui.BrowseButton.clicked.connect(self.Browse)

    def CopyEntry(self):
        Nametext = self.ui.NameEdit.text()
        self.ui.IterationEdit.setText(Nametext)

    def Browse(self):
        xmlFile = QtGui.QFileDialog.getOpenFileName(self,'Open File', '', 'XML File(*.xml)')
        self.ui.XMLPathEdit.setText(xmlFile)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = XMLManager()
    myapp.show()
    sys.exit(app.exec_())