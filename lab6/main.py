from math import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QPointF, QEventLoop
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
import sys
import time

size_x = 1150
size_y = 900


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = Scene(0, 0, size_x, size_y)
        self.canvas.setScene(self.scene)

        self.image = QImage(size_x, size_y, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(Qt.white)
        self.pen = QPen(Qt.black)

        self.end_polygon_bt.clicked.connect(lambda: close_polygon())
        self.add_point_bt.clicked.connect(lambda: add_sb_point(self))
        self.clear_bt.clicked.connect(lambda: clear(self))
        self.add_seed_pix_bt.clicked.connect(lambda: get_seed_pix(self))
        self.fill_bt.clicked.connect(lambda: fill_polygon(self))

        self.color_bg_bt.clicked.connect(lambda: get_bg_color(self))
        self.color_seed_bt.clicked.connect(lambda: get_seed_color(self))
        self.color_border_bt.clicked.connect(lambda: get_border_color(self))

        self.seed_pix_button_clicked = False
        self.cur_polygon = list()

        self.bg_color = QColor(Qt.white)
        self.border_color = QColor(Qt.black)
        self.seed_color = QColor(229, 204, 255)
        self.first_color_buttons()

        draw_frame(self)

    def first_color_buttons(self):
        self.color_bg_bt.setStyleSheet("background-color:rgb"
                                       + color_in_str(self.bg_color.getRgb()))
        self.color_seed_bt.setStyleSheet("background-color:rgb"
                                         + color_in_str(self.seed_color.getRgb()))
        self.color_border_bt.setStyleSheet("background-color:rgb"
                                           + color_in_str(self.border_color.getRgb()))


class Scene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.modifiers() == Qt.ShiftModifier:
            add_straight_point(event.scenePos())
        elif event.buttons() == Qt.LeftButton:
            add_point(event.scenePos())
        elif event.buttons() == Qt.RightButton:
            close_polygon()
        else:
            fill_polygon_m()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.modifiers() == Qt.ShiftModifier:
            add_straight_point(event.scenePos())
        elif event.buttons() == Qt.LeftButton:
            add_point(event.scenePos())
        elif event.buttons() == Qt.RightButton:
            close_polygon()


def color_in_str(color):
    return str("(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")")


def get_seed_pix(window):
    window.seed_pix_button_clicked = True


def fill_polygon_m():
    global window
    fill_polygon(window)


def add_point(point):
    global window

    if point.x() < 0 or point.y() < 0 or point.x() > size_x - 1 or point.y() > size_y - 1:
        return

    if window.seed_pix_button_clicked:
        window.x_z_sb.setValue(point.x())
        window.y_z_sb.setValue(point.y())
        window.seed_pix_button_clicked = False
        return

    rows = window.all_points_table.rowCount()
    window.all_points_table.insertRow(rows)
    index = rows - 1

    window.all_points_table.setItem(index, 0, QtWidgets.QTableWidgetItem(str(point.x())))
    window.all_points_table.setItem(index, 1, QtWidgets.QTableWidgetItem(str(point.y())))
    window.cur_polygon.append(point)

    size = len(window.cur_polygon)

    if size > 1:
        cda(window, window.cur_polygon[size - 2].x(),
            window.cur_polygon[size - 2].y(),
            window.cur_polygon[size - 1].x(),
            window.cur_polygon[size - 1].y(),
            QPen(window.border_color).color().rgba())
        window.scene.clear()
        draw_image_from_pix(window)


def add_straight_point(point):
    global window

    size = len(window.cur_polygon)

    if size == 0:
        add_point(point)

    else:
        last_point = window.cur_polygon[size - 1]
        k1 = fabs(point.y() - last_point.y())
        k2 = fabs(last_point.x() - point.x())

        if k2 == 0:
            add_point(QPointF(point.x(), last_point.y()))
        elif fabs(degrees(atan(k1 / k2))) <= 45:
            add_point(QPointF(point.x(), last_point.y()))
        else:
            add_point(QPointF(last_point.x(), point.y()))


def add_sb_point(window):
    add_point(QPointF(window.x_sb.value(), window.y_sb.value()))


def close_polygon():
    global window
    color = QPen(window.border_color).color().rgba()

    size = len(window.cur_polygon)
    if size > 2:
        cda(window, window.cur_polygon[size - 1].x(),
            window.cur_polygon[size - 1].y(),
            window.cur_polygon[0].x(),
            window.cur_polygon[0].y(),
            color)

        draw_image_from_pix(window)
        window.cur_polygon = list()


def fill_part(x, y, x_right, seed_color, border_color, stack):
    while x <= x_right:
        flag = False
        cur_pix_color = window.image.pixel(x, y)

        while cur_pix_color != seed_color and cur_pix_color != border_color and x <= x_right:
            if not flag:
                flag = True
            x += 1
            cur_pix_color = window.image.pixel(x, y)

        if flag:
            if x == x_right and cur_pix_color != border_color and cur_pix_color != seed_color:
                stack.append(QPointF(x, y))
            else:
                stack.append(QPointF(x - 1, y))

        x_last = x
        while (cur_pix_color == border_color or cur_pix_color == seed_color) and x < x_right:
            x += 1
            cur_pix_color = window.image.pixel(x, y)

        if x == x_last:
            x = x + 1


def fill_polygon(window):

    stack = list()
    seed = QPointF(window.x_z_sb.value(), window.y_z_sb.value())
    if not check_pixel(seed):
        QMessageBox.warning(window, "Ошибка", "Затравочный пиксель находится вне рамки или на ней")
        return

    border_color = window.border_color.rgb()
    seed_color = window.seed_color.rgb()
    need_delay = window.delay.checkState()

    st = time.clock()

    stack.append(seed)

    while stack:
        pixel = stack.pop()
        x = pixel.x()
        y = pixel.y()
        temp_x = x
        window.image.setPixel(x, y, seed_color)

        x += 1
        while window.image.pixel(x, y) != border_color:
            window.image.setPixel(x, y, seed_color)
            x += 1

        x_right = x - 1
        x = temp_x

        x -= 1
        while window.image.pixel(x, y) != border_color:
            window.image.setPixel(x, y, seed_color)
            x -= 1

        x_left = x + 1

        fill_part(x_left, y + 1, x_right, seed_color, border_color, stack)

        fill_part(x_left, y - 1, x_right, seed_color, border_color, stack)

        if need_delay:
            delay()
            window.scene.clear()
            draw_image_from_pix(window)

    t = time.clock() - st

    window.scene.clear()
    draw_image_from_pix(window)

    QMessageBox.information(window, "Время выполнения", str(t) + " msc")


def draw_image_from_pix(window):
    pixel = QPixmap(size_x, size_y)
    pixel.convertFromImage(window.image)
    window.scene.addPixmap(pixel)


def clear(window):
    rows = window.all_points_table.rowCount()
    for i in range(rows - 1, -1, -1):
        window.all_points_table.removeRow(i)
    window.all_points_table.insertRow(0)
    window.scene.clear()
    window.image.fill(window.bg_color)
    window.cur_polygon = list()
    draw_frame(window)


def round_number(number):
    return int(number + 0.5)


def cda(window, x0, y0, xk, yk, color):
    dx = xk - x0
    dy = yk - y0

    x = x0
    y = y0

    if fabs(dx) > fabs(dy):
        len_line = fabs(dx)
    else:
        len_line = fabs(dy)

    if len_line == 0:
        window.image.setPixel(x, y, color)
        return

    sx = dx / len_line
    sy = dy / len_line
    i = len_line
    window.image.setPixel(round_number(xk), round_number(yk), color)

    while i > 0:
        window.image.setPixel(round_number(x), round_number(y), color)
        x += sx
        y += sy
        i -= 1


def delay():
    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents)


def check_pixel(point):
    return not (point.x() <= 0 or point.y() <= 0 or point.x() >= size_x or point.y() >= size_y)


def get_bg_color(window):
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        if color == window.border_color:
            QMessageBox.warning(window, "Ошибка", "Цвет фона и цвет границы совпадают")
            return

        window.bg_color = color
        window.color_bg_bt.setStyleSheet("background-color:rgb"
                                         + color_in_str(window.bg_color.getRgb()))
        fill_bg(window)


def get_seed_color(window):
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        window.seed_color = color
        window.color_seed_bt.setStyleSheet("background-color:rgb"
                                           + color_in_str(window.seed_color.getRgb()))


def get_border_color(window):
    color = QtWidgets.QColorDialog.getColor()
    if color.isValid():
        if color == window.bg_color:
            QMessageBox.warning(window, "Ошибка", "Цвет фона и цвет границы совпадают")
            return

        window.border_color = color
        window.color_border_bt.setStyleSheet("background-color:rgb"
                                             + color_in_str(window.border_color.getRgb()))
        draw_frame(window)


def fill_bg(window):
    window.image.fill(window.bg_color)
    window.scene.clear()
    draw_image_from_pix(window)
    draw_frame(window)


def draw_frame(window):
    color = QPen(window.border_color).color().rgba()

    cda(window, 0, 0, size_x, 0, color)
    cda(window, 0, 0, 0, size_y - 1, color)
    cda(window, size_x - 1, 0, size_x - 1, size_y - 1, color)
    cda(window, 0, size_y - 1, size_x, size_y - 1, color)

    window.scene.clear()
    draw_image_from_pix(window)


def main():
    global window

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
