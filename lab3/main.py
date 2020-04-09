'''
 Лабораторная №3
 Реализация и исследование алгоритмов построения отрезков:
    1. Рисование отдельных отрезков и сравнение их визуальных характеристик
    2. Исследование визуальных характеристик для отрезков,
       распространенных во всем спектре изменения углов
    3. Исследование временных характеристик в виде гистограммы
    4. Исследование ступенчатости
'''

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64
from PyQt5.QtCore import Qt
from math import cos, sin, pi, radians, copysign, fabs, trunc
import numpy as np
import time

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = QtWidgets.QGraphicsScene(0, 0, 511, 511)
        self.mainview.setScene(self.scene)
        self.image = QImage(511, 511, QImage.Format_ARGB32_Premultiplied)
        self.pen = QPen()
        self.color_line = QColor(Qt.black)
        self.color_bground = QColor(Qt.white)
        self.draw_line.clicked.connect(lambda: draw_line(self))
        self.clean_all.clicked.connect(lambda : clear_all(self))
        self.btn_bground.clicked.connect(lambda: get_color_bground(self))
        self.btn_line.clicked.connect(lambda: get_color_line(self))
        self.draw_sun.clicked.connect(lambda: draw_beam(self))
        self.cda.setChecked(True)

def sign(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)


def line_CDA(win, p1, p2):

    length = max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

    if length == 0:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    dX = (p2[0] - p1[0]) / length
    dY = (p2[1] - p1[1]) / length

    x = p1[0] + 0.5 * sign(dX)
    y = p1[1] + 0.5 * sign(dY)

    while length > 0:
        win.image.setPixel(x, y, win.pen.color().rgb())
        x += dX
        y += dY
        length -= 1


def line_br_float(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]
    ch = 0
    if dy > dx:
        dx, dy = dy, dx
        ch = 1
    h = dy / dx
    e = h - 0.5
    i = 1

    while i <= dx:
        win.image.setPixel(x, y, win.pen.color().rgb())
        if e >= 0:
            if not ch:
                y += sy
            else:
                x += sx
            e -= 1

        if e < 0:
            if not ch:
                x += sx
            else:
                y += sy
            e += h
        i += 1


def line_br_int(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]
    ch = 0
    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        ch = 1

    e = 2 * dy - dx
    i = 1
    while i <= dx:
        win.image.setPixel(x, y, win.pen.color().rgb())
        if e >= 0:
            if ch == 0:
                y += sy
            else:
                x += sx
            e -= 2 * dx

        if e < 0:
            if ch == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)
        i += 1


def line_br_smooth(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return
    win.pen.setColor(win.color_line)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    try:
        h = dy / dx
    except ZeroDivisionError:
        h = 0

    isBlack = 0

    if win.pen.color() == Qt.black:
        i_max = 256
        isBlack = True
    else:
        i_max = 100

    change = 0

    if dy > dx:
        dx, dy = dy, dx
        change = 1
        if h:
            h = 1 / h

    h *= i_max
    e = i_max/2
    w = i_max - h
    i = 1
    while i <= dx:
        if not isBlack:
            new = win.pen.color()
            new.lighter(100 + e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        else:
            new = QColor()
            new.setRgb(0, 0, 0, alpha=255 - e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i += 1



def line_draw_Wu(win, p1, p2):
    color = win.pen.color()

    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    dx = x2 - x1
    dy = y2 - y1
    max_i = 255
    m = sys.maxsize

    if abs(dy) > abs(dx):
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if dy != 0:
            m = dx / dy
        y1 = round(y1)
        y2 = round(y2)
        x = x1
        y = y1
        while y < y2 + 1:
            d1 = x - trunc(x)
            d2 = 1 - d1
            color.setAlpha(int(max_i * d2))
            win.image.setPixel(trunc(x), y, color.rgba())
            color.setAlpha(int(max_i * d1))
            win.image.setPixel(trunc(x) + 1, y, color.rgba())
            x += m
            y += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if dx != 0:
            m = dy / dx
        x1 = round(x1)
        x2 = round(x2)
        x = x1
        y = y1
        while x < x2 + 1:
            d1 = y - trunc(y)
            d2 = 1 - d1

            color.setAlpha(int(max_i * d2))  # Интенсивность
            win.image.setPixel(x, trunc(y), color.rgba())
            color.setAlpha(int(max_i * d1))
            win.image.setPixel(x, trunc(y) + 1, color.rgba())
            y += m
            x += 1


def draw_line(win):
    bx = win.begin_x.value()
    by = win.begin_y.value()
    ex = win.end_x.value()
    ey = win.end_y.value()
    is_standart = False
    win.image.fill(win.color_bground)
    if win.cda.isChecked():
        start = time.clock()
        line_CDA(win, [bx, by], [ex, ey])
        end = time.clock()
    if win.br_float.isChecked():
        start = time.clock()
        line_br_float(win, [bx, by], [ex, ey])
        end = time.clock()
    if win.br_int.isChecked():
        start = time.clock()
        line_br_int(win, [bx, by], [ex, ey])
        end = time.clock()
    if win.br_smooth.isChecked():
        start = time.clock()
        line_br_smooth(win, [bx, by], [ex, ey])
        end = time.clock()
    if win.lib.isChecked():
        #is_standart = True
        start = time.clock()
        line_draw_Wu(win, [bx, by], [ex, ey])
        #win.scene.addLine(bx, by, ex, ey, win.pen)
        end = time.clock()

    if not is_standart:
        pix = QPixmap(511, 511)
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)

    #win.label.setText("{0:.3f}msc".format((end - start)*1000))


def draw_beam(win):
    d = win.spin_dia.value()
    spin = win.spin_angle.value()
    bx = 255
    by = 255
    #win.image.fill(win.color_bground)
    is_standart = False
    for i in np.arange(0, 360, spin):
        ex = cos(radians(i)) * d + 255
        ey = sin(radians(i)) * d + 255

        if win.cda.isChecked():
            start = time.clock()
            line_CDA(win, [bx, by], [ex, ey])
            end = time.clock()
        if win.br_float.isChecked():
            start = time.clock()
            line_br_float(win, [bx, by], [ex, ey])
            end = time.clock()
        if win.br_int.isChecked():
            start = time.clock()
            line_br_int(win, [bx, by], [ex, ey])
            end = time.clock()
        if win.br_smooth.isChecked():
            start = time.clock()
            line_br_smooth(win, [bx, by], [ex, ey])
            end = time.clock()
        if win.lib.isChecked():
            #is_standart = True
            start = time.clock()
            line_draw_Wu(win, [bx, by], [ex, ey])
            #win.scene.addLine(bx, by, ex, ey, win.pen)
            end = time.clock()

    if not is_standart:
        pix = QPixmap(511, 511)
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)

    print("{0:.3f}msc".format((end - start) * 1000))


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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
