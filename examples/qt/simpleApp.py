from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mainApp import Ui_MainWindow
from simpleForm import Ui_Tab1Form

class SimpleApp(QMainWindow):

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        formWidget = QWidget()
        formWidget.ui = Ui_Tab1Form()
        formWidget.ui.setupUi(formWidget)

        self.ui.tabWidget.removeTab(1)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(formWidget,"Color Preference")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    td = SimpleApp()
    td.show()
    sys.exit(app.exec_())