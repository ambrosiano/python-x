# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myTableDialog.ui'
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

class Ui_MyTableDialog(object):
    def setupUi(self, MyTableDialog):
        MyTableDialog.setObjectName(_fromUtf8("MyTableDialog"))
        MyTableDialog.resize(873, 724)
        self.gridLayout_2 = QtGui.QGridLayout(MyTableDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.headlabel = QtGui.QLabel(MyTableDialog)
        self.headlabel.setObjectName(_fromUtf8("headlabel"))
        self.gridLayout.addWidget(self.headlabel, 0, 0, 1, 1)
        self.authorlabel = QtGui.QLabel(MyTableDialog)
        self.authorlabel.setObjectName(_fromUtf8("authorlabel"))
        self.gridLayout.addWidget(self.authorlabel, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(MyTableDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.titlelabel = QtGui.QLabel(MyTableDialog)
        self.titlelabel.setObjectName(_fromUtf8("titlelabel"))
        self.gridLayout.addWidget(self.titlelabel, 1, 0, 1, 1)
        self.authorlineEdit = QtGui.QLineEdit(MyTableDialog)
        self.authorlineEdit.setObjectName(_fromUtf8("authorlineEdit"))
        self.gridLayout.addWidget(self.authorlineEdit, 2, 1, 1, 1)
        self.titlelineEdit = QtGui.QLineEdit(MyTableDialog)
        self.titlelineEdit.setObjectName(_fromUtf8("titlelineEdit"))
        self.gridLayout.addWidget(self.titlelineEdit, 1, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(MyTableDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 845, 574))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableView = QtGui.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.authorlabel.setBuddy(self.authorlineEdit)
        self.titlelabel.setBuddy(self.titlelineEdit)

        self.retranslateUi(MyTableDialog)
        QtCore.QMetaObject.connectSlotsByName(MyTableDialog)

    def retranslateUi(self, MyTableDialog):
        MyTableDialog.setWindowTitle(_translate("MyTableDialog", "Dialog", None))
        self.headlabel.setText(_translate("MyTableDialog", "Books", None))
        self.authorlabel.setText(_translate("MyTableDialog", "Author", None))
        self.titlelabel.setText(_translate("MyTableDialog", "Title", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MyTableDialog = QtGui.QDialog()
    ui = Ui_MyTableDialog()
    ui.setupUi(MyTableDialog)
    MyTableDialog.show()
    sys.exit(app.exec_())

