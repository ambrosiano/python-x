# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pan_zoom_image_dialog.ui'
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

class Ui_PanZoomImageDialog(object):
    def setupUi(self, PanZoomImageDialog):
        PanZoomImageDialog.setObjectName(_fromUtf8("PanZoomImageDialog"))
        PanZoomImageDialog.resize(600, 400)
        self.gridLayout = QtGui.QGridLayout(PanZoomImageDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(PanZoomImageDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 347))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.chooseImageButton = QtGui.QPushButton(PanZoomImageDialog)
        self.chooseImageButton.setObjectName(_fromUtf8("chooseImageButton"))
        self.gridLayout.addWidget(self.chooseImageButton, 1, 0, 1, 1)

        self.retranslateUi(PanZoomImageDialog)
        QtCore.QMetaObject.connectSlotsByName(PanZoomImageDialog)

    def retranslateUi(self, PanZoomImageDialog):
        PanZoomImageDialog.setWindowTitle(_translate("PanZoomImageDialog", "Dialog", None))
        self.chooseImageButton.setText(_translate("PanZoomImageDialog", "Choose Image", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PanZoomImageDialog = QtGui.QDialog()
    ui = Ui_PanZoomImageDialog()
    ui.setupUi(PanZoomImageDialog)
    PanZoomImageDialog.show()
    sys.exit(app.exec_())

