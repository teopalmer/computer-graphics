'''
 Лабораторная №4
 Реализация алгоритмов построения окружности, исследование
 и сравнение визуальных и временных характеристик алгоритмов.
'''

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64
from PyQt5.QtCore import Qt
from math import cos, sin, pi, radians, copysign, fabs, trunc
import numpy as np
import time
import algs as al

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = QtWidgets.QGraphicsScene(0, 0, 511, 511)
        self.canvas.setScene(self.scene)
        self.image = QImage(511, 511, QImage.Format_ARGB32_Premultiplied)
        self.pen = QPen()
        self.color_line = QColor(Qt.black)
        self.color_bground = QColor(Qt.white)
        self.clean_all.clicked.connect(lambda : clear_all(self))
        self.bgColorButton.clicked.connect(lambda: get_color_bground(self))
        self.lineColorButton.clicked.connect(lambda: get_color_line(self))
        self.roundButton.clicked.connect(lambda: draw_circle(self))
        self.ellipseButton.clicked.connect(lambda: draw_ellipse(self))

def get_color_bground(win):
    color = QtWidgets.QColorDialog.getColor(initial=Qt.white, title='Цвет фона',
                                            options=QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.color_bground = color
        win.image.fill(color)
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.bground_color.setScene(s)
        win.scene.setBackgroundBrush(color)


def get_color_line(win):
    color = QtWidgets.QColorDialog.getColor(initial=Qt.black, title='Цвет линии',
                                            options=QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.color_line = color
        win.pen.setColor(color)
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.line_color.setScene(s)

def clear_all(win):
    win.image.fill(Qt.color0)
    win.scene.clear()

def draw_circle(win):
    win.image.setPixel(255, 255, 255)
    x = win.RXspinBox.value()
    y = win.RYspinBox.value()
    r = win.RRspinBox.value()

    win.image.fill(win.color_bground)

    start = time.clock()
    if win.canonButton.isChecked():
        al.circle_canon(win, x, y, r)
    if win.paramButton.isChecked():
        al.circle_param(win, x, y, r)
    if win.brezButton.isChecked():
        al.circle_brez(win, x, y, r)
    if win.middleButton.isChecked():
        al.circle_middle(win, x, y, r)
    if win.libraryButton.isChecked():
        win.scene.addEllipse(x - r, y - r, r * 2, r * 2, win.pen)
    end = time.clock()

def draw_ellipse(win):
    x = win.EXspinBox.value()
    y = win.EYspinBox.value()
    a = win.EHXspinBox.value()
    b = win.EHYspinBox.value()

    win.image.fill(win.color_bground)

    start = time.clock()
    if win.canonButton.isChecked():
        al.draw_canon(win, x, y, b, a)
    if win.paramButton.isChecked():
        al.draw_param(win, x, y, b, a)
    if win.brezButton.isChecked():
        al.draw_brez(win, x, y, b, a)
    if win.middleButton.isChecked():
        al.draw_middle(win, x, y, b, a)
    if win.libraryButton.isChecked():
        win.scene.addEllipse(x - b, y - a, b * 2, a * 2, win.pen)
    end = time.clock()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

