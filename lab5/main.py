from math import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QPointF, QEventLoop
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("interface.ui", self)
        self.scene = Scene(0, 0, 4000, 4000)
        self.canvas.setScene(self.scene)

        self.image = QImage(4000, 4000, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        self.pen = QPen(Qt.black)
        self.all_polygons = list()
        self.cur_polygon = list()


class Scene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.modifiers() == Qt.ShiftModifier:
            add_straight_point(event.scenePos())

