from PyQt4.QtGui import *
from PyQt4.QtCore import *
from myTableDialog import *
from tables import TableModel

class TableDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_MyTableDialog()
        self.ui.setupUi(self)

        tabledata = [["",""]]#[["Frankenstein","Mary Shelley"]]
        headers = ["Title","Author"]
        self.tablemodel = TableModel(tabledata,headers)
        self.ui.tableView.setModel(self.tablemodel)
        self.ui.tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.ui.buttonBox.rejected.connect(self.cancelAction)
        self.ui.buttonBox.accepted.connect(self.okAction)

    def clearForm(self):
        self.ui.authorlineEdit.clear()
        self.ui.titlelineEdit.clear()

    def cancelAction(self):
        print("Cancel action.")
        self.clearForm()

    def okAction(self):
        print("OK action")
        author = self.ui.authorlineEdit.text()
        title = self.ui.titlelineEdit.text()
        tm = self.tablemodel
        data = tm.arraydata
        record = [title,author]
        n = tm.rowCount(None)
        if n==1 & (data[0] == ["",""]):
            data[0] = record
        else:
            data.append(record)
        tm.emit(SIGNAL("layoutChanged()"))
        self.clearForm()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    td = TableDialog()
    td.show()
    sys.exit(app.exec_())