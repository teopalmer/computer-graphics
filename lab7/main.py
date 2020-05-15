from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
import time

red = Qt.red
blue = Qt.blue
now = None

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = Scene(0, 0, 561, 581)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        self.lines = []
        self.clip = None
        self.point_now = None
        self.input_bars = False
        self.input_rect = False
        self.pen = QPen(red)


class Scene(QtWidgets.QGraphicsScene):

    def mousePressEvent(self, event):
        add_point(event.scenePos())

def add_point(point):
    global w
    if w.input_bars:
        if w.point_now is None:
            w.point_now = point
        else:
            w.lines.append([[w.point_now.x(), w.point_now.y()],
                            [point.x(), point.y()]])

            i = w.table.rowCount() - 1
            item_b = QTableWidgetItem("[{0}, {1}]".format(w.point_now.x(), w.point_now.y()))
            item_e = QTableWidgetItem("[{0}, {1}]".format(point.x(), point.y()))
            w.table.setItem(i, 0, item_b)
            w.table.setItem(i, 1, item_e)
            w.scene.addLine(w.point_now.x(), w.point_now.y(), point.x(), point.y(), w.pen)
            w.point_now = None
