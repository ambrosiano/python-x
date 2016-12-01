# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleForm.ui'
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

class Ui_SimpleForm(object):
    def setupUi(self, SimpleForm):
        SimpleForm.setObjectName(_fromUtf8("SimpleForm"))
        SimpleForm.resize(697, 415)
        self.gridLayout = QtGui.QGridLayout(SimpleForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(SimpleForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(SimpleForm)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(SimpleForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(SimpleForm)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(SimpleForm)
        QtCore.QMetaObject.connectSlotsByName(SimpleForm)

    def retranslateUi(self, SimpleForm):
        SimpleForm.setWindowTitle(_translate("SimpleForm", "Colors", None))
        self.label.setText(_translate("SimpleForm", "Name", None))
        self.label_2.setText(_translate("SimpleForm", "Color Preference", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SimpleForm = QtGui.QWidget()
    ui = Ui_SimpleForm()
    ui.setupUi(SimpleForm)
    SimpleForm.show()
    sys.exit(app.exec_())

