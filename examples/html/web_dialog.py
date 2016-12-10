# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web_dialog.ui'
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

class Ui_WebDialog(object):
    def setupUi(self, WebDialog):
        WebDialog.setObjectName(_fromUtf8("WebDialog"))
        WebDialog.resize(600, 400)
        self.gridLayout = QtGui.QGridLayout(WebDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(WebDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.choosePageButton = QtGui.QPushButton(WebDialog)
        self.choosePageButton.setObjectName(_fromUtf8("choosePageButton"))
        self.gridLayout.addWidget(self.choosePageButton, 1, 0, 1, 1)

        self.retranslateUi(WebDialog)
        QtCore.QMetaObject.connectSlotsByName(WebDialog)

    def retranslateUi(self, WebDialog):
        WebDialog.setWindowTitle(_translate("WebDialog", "Dialog", None))
        self.choosePageButton.setText(_translate("WebDialog", "Choose Page", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WebDialog = QtGui.QDialog()
    ui = Ui_WebDialog()
    ui.setupUi(WebDialog)
    WebDialog.show()
    sys.exit(app.exec_())

