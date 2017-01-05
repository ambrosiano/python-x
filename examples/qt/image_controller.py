from PyQt4.QtGui import *
from PyQt4.QtCore import *
from image_dialog import Ui_ImageDialog


class ImageController(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)

        self.connect(self.ui.chooseImageButton, SIGNAL("clicked()"), self.chooseimage_action)

    def chooseimage_action(self):
        print("Show Image")
        imagefile = QFileDialog.getOpenFileName(self)
        pixmap = QPixmap()
        pixmap.load(imagefile)
        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = ImageController()
    w.show()
    sys.exit(app.exec_())