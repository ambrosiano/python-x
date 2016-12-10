# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_dialog.ui'
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

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName(_fromUtf8("ImageDialog"))
        ImageDialog.resize(600, 400)
        self.gridLayout = QtGui.QGridLayout(ImageDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(ImageDialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.chooseImageButton = QtGui.QPushButton(ImageDialog)
        self.chooseImageButton.setObjectName(_fromUtf8("chooseImageButton"))
        self.gridLayout.addWidget(self.chooseImageButton, 1, 0, 1, 1)

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Dialog", None))
        self.chooseImageButton.setText(_translate("ImageDialog", "Choose Image", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageDialog = QtGui.QDialog()
    ui = Ui_ImageDialog()
    ui.setupUi(ImageDialog)
    ImageDialog.show()
    sys.exit(app.exec_())

