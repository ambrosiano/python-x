from PyQt4.QtGui import *
from PyQt4.QtCore import *




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = QInputDialog()
    dialog.setComboBoxItems(QStringList(["one","two"]))
    dialog.setWindowTitle("Select")
    dialog.setLabelText("Choices")
    if dialog.exec_():
        print(str(dialog.textValue()))


    sys.exit(app.exec_())