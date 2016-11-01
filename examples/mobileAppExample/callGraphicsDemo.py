import sys
from graphicsViewDemo import *
from PyQt4.QtGui import *
class MyForm(QtGui.QDialog):
 def __init__(self, pixmap, parent=None):
  QtGui.QWidget.__init__(self, parent)
  self.ui = Ui_Dialog()
  self.ui.setupUi(self)
  self.scene = QGraphicsScene(self)
  item=QGraphicsPixmapItem(pixmap)
  self.scene.addItem(item)
  self.ui.graphicsView.setScene(self.scene)

if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   pixmap= QtGui.QPixmap()
   pixmap.load("bmpic.jpg")
   myapp = MyForm(pixmap)
   myapp.show()
   sys.exit(app.exec_())
