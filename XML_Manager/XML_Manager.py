import sys
from XML_Parser import XML_Parser 
from PyQt4 import QtCore, QtGui
from XML_ManagerWindow import Ui_XMLManager

class XMLManager(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_XMLManager()
        self.ui.setupUi(self)
        #self.ui.OkButton.clicked.connect(lambda: self.addBenchmark({str(self.ui.NameEdit.text()):str(self.ui.IterationEdit.text())}))
        self.ui.ApplyButton.clicked.connect(self.saveFile)
        self.ui.BrowseButton.clicked.connect(self.browse)

    def browse(self):
        self.xmlFilePath = QtGui.QFileDialog.getOpenFileName(self,'Open File', '', 'XML File(*.xml)')
        self.ui.XMLPathEdit.setText(self.xmlFilePath)
        self.parseFile()
         
    def parseFile(self):
        self.benchmarkXmlDoc = XML_Parser(str(self.xmlFilePath))
        self.__fillTable()

    def addBenchmark(self, benchMap):
        self.benchmarkXmlDoc.addBenchmark(benchMap)

    def saveFile(self):
        self.benchmarkXmlDoc.writeFile()
        
    def __fillTable(self):

        items = self.benchmarkXmlDoc.benchmarksMap.items()
        self.ui.tableWidget.setRowCount(len(items))
        self.ui.tableWidget.setColumnCount(2)
        
        for i in range(len(items)):
            self.ui.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(items[i][0]))
            self.ui.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(items[i][1]))
            


        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = XMLManager()
    myapp.show()
    sys.exit(app.exec_())