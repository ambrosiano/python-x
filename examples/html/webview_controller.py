from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from web_dialog import Ui_WebDialog

class WebViewController(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_WebDialog()
        self.ui.setupUi(self)

        self.webview = QWebView()
        layout = QGridLayout()

        self.ui.frame.setLayout(layout)
        layout.addWidget(self.webview)

        self.connect(self.ui.choosePageButton, SIGNAL("clicked()"), self.choosepage_action)

    def choosepage_action(self):
        print("Choose Web Page")
        htmlfile = QFileDialog.getOpenFileName(self)
        print(htmlfile)
        self.webview.load(QUrl("file:///"+htmlfile))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = WebViewController()
    w.show()
    sys.exit(app.exec_())