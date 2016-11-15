from PyQt4.QtGui import *
from myTableDialog import *
from tables import TableModel

class TableDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_MyTableDialog()
        self.ui.setupUi(self)

        tabledata = [["Frankenstein","Mary Shelley"]]
        headers = ["Title","Author"]
        self.tablemodel = TableModel(tabledata,headers)
        self.ui.tableView.setModel(self.tablemodel)

        self.ui.buttonBox.rejected.connect(self.cancelAction)
        self.ui.buttonBox.accepted.connect(self.okAction)


    def cancelAction(self):
        print("Cancel action.")


    def okAction(self):
        print("OK action")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    td = TableDialog()
    td.show()
    sys.exit(app.exec_())