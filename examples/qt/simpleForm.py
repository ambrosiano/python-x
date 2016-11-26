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

class Ui_Tab1Form(object):
    def setupUi(self, Tab1Form):
        Tab1Form.setObjectName(_fromUtf8("Tab1Form"))
        Tab1Form.resize(698, 415)
        self.gridLayout = QtGui.QGridLayout(Tab1Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Tab1Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(Tab1Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(Tab1Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(Tab1Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Tab1Form)
        QtCore.QMetaObject.connectSlotsByName(Tab1Form)

    def retranslateUi(self, Tab1Form):
        Tab1Form.setWindowTitle(_translate("Tab1Form", "Form", None))
        self.label.setText(_translate("Tab1Form", "Name", None))
        self.label_2.setText(_translate("Tab1Form", "Color Preference", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Tab1Form = QtGui.QWidget()
    ui = Ui_Tab1Form()
    ui.setupUi(Tab1Form)
    Tab1Form.show()
    sys.exit(app.exec_())

