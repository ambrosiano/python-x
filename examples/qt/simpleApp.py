from PyQt4.QtGui import *
from PyQt4.QtCore import *

from myMainWindow import Ui_MainWindow
from simpleForm import Ui_SimpleForm

class SimpleApp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout = self.ui.centralwidget.layout()

        tabWidget = QTabWidget()
        layout.addWidget(tabWidget)


        formWidget = QWidget()
        formWidget.ui = Ui_SimpleForm()
        formWidget.ui.setupUi(formWidget)

        tabWidget.addTab(formWidget,"Color Preference")

        # self.ui.tabWidget.removeTab(1)
        # self.ui.tabWidget.removeTab(0)
        # self.ui.tabWidget.addTab(formWidget,"Color Preference")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    td = SimpleApp()
    td.show()
    sys.exit(app.exec_())