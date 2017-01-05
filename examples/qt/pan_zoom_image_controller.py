from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pan_zoom_image_dialog import Ui_PanZoomImageDialog


class PhotoViewer(QGraphicsView):
    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._scene = QGraphicsScene(self)
        self._photo = QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        self.setFrameShape(QFrame.NoFrame)

    def fitInView(self):
        rect = QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
            self.scale(1 / unity.width(), 1 / unity.height())
            viewrect = self.viewport().rect()
            scenerect = self.transform().mapRect(rect)
            factor = min(viewrect.width() / scenerect.width(),
                         viewrect.height() / scenerect.height())
            self.scale(factor, factor)
            self.centerOn(rect.center())
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
            self.fitInView()
        else:
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())

    def zoomFactor(self):
        return self._zoom

    def wheelEvent(self, event):
        if not self._photo.pixmap().isNull():
            if event.delta() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0


class PanZoomImageController(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = Ui_PanZoomImageDialog()
        self.ui.setupUi(self)

        self.connect(self.ui.chooseImageButton, SIGNAL("clicked()"), self.chooseimage_action)

    def chooseimage_action(self):
        print("Show Image")
        imagefile = QFileDialog.getOpenFileName(self)
        pixmap = QPixmap()
        pixmap.load(imagefile)
        scrollArea = self.ui.scrollArea

        panZoomView = PhotoViewer(scrollArea)
        scrollArea.setWidget(panZoomView)

        panZoomView.setPhoto(pixmap)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = PanZoomImageController()
    w.show()
    sys.exit(app.exec_())