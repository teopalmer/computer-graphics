from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
import sys
global w

global pen_color
global bg_color

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = myScene(0, 0, 561, 581)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.bgColorButton.clicked.connect(lambda: get_color_bground(self))

        self.image.fill(bg_color)
        self.lock.clicked.connect(lambda: lock(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: fill_polygon(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))

        self.edges = []
        self.point_now = None
        self.point_start = None
        self.pen = QPen(pen_color)
        self.delay.setChecked(False)


class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            add_point(event.scenePos())
        else:
            lock(w)


def get_color_bground(win):
    global pen_color
    color = QtWidgets.QColorDialog.getColor(initial=Qt.black, title='Цвет фона',
                                            options=QtWidgets.QColorDialog.DontUseNativeDialog)
    if color.isValid():
        win.color_bground = color
        s = QtWidgets.QGraphicsScene(0, 0, 10, 10)
        s.setBackgroundBrush(color)
        win.bground_color.setScene(s)
        pen_color = color


def add_row(win):
    win.table.insertRow(win.table.rowCount())


def add_point(point):
    if not w.point_now:
        w.point_start = point
    else:
        w.edges.append([w.point_now.x(), w.point_now.y(),
                        point.x(), point.y()])
        w.scene.addLine(w.point_now.x(), w.point_now.y(),
                        point.x(), point.y(), w.pen)

    w.point_now = point
    i = w.table.rowCount()
    add_row(w)
    x = QTableWidgetItem("{0}".format(point.x()))
    y = QTableWidgetItem("{0}".format(point.y()))
    w.table.setItem(i, 0, x)
    w.table.setItem(i, 1, y)


def lock(win):
    x1, y1 = win.point_now.x(), win.point_now.y()
    x2, y2 = win.point_start.x(), win.point_start.y()

    win.edges.append([x1, y1, x2, y2])
    win.scene.addLine(x1, y1, x2, y2, w.pen)

    win.point_now = None

def draw_circle(image, rad, point):
    p = QPainter()
    p.begin(image)
    p.setPen(QPen(QColor(0, 0, 255)))
    p.drawEllipse(point.x() - rad, point.y() - rad, rad * 2, rad * 2)
    p.end()

def get_pixel(point):
    global w, point_zat, circle
    pix = QPixmap()
    if circle:
        r = w.rad.value()
        draw_circle(w.image, r, point)
        circle = False
    if point_zat:
        w.p_x.setValue(point.x())
        w.p_y.setValue(point.y())
        draw_edges(w.image, w.edges)
        point_zat = False
    pix.convertFromImage(w.image)
    w.scene.addPixmap(pix)
    w.lock.setDisabled(False)
    w.erase.setDisabled(False)
    w.paint.setDisabled(False)
    w.addpoint.setDisabled(False)
    w.addcircle.setDisabled(False)
    w.pixel.setDisabled(False)


def clean_all(win):
    l = win.table.rowCount()
    for i in range(l, -1, -1):
        win.table.removeRow(i)

    win.scene.clear()
    win.table.clearContents()
    win.edges = []
    win.point_now = None
    win.point_start = None
    win.image.fill(bg_color)


def draw_edges(image, edges):
    p = QPainter()
    p.begin(image)
    p.setPen(QPen(pen_color))
    for e in edges:
        p.drawLine(e[0], e[1], e[2], e[3])
    p.end()


def delay(win, pix):
    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 1)
    pix.convertFromImage(win.image)
    win.scene.addPixmap(pix)


def find_max_x(edges):
    xm = None
    
    for i in range(len(edges)):
        if not xm or edges[i][0] > xm:
            xm = edges[i][0]

        if not xm or edges[i][2] > xm:
            xm = edges[i][2]

    return xm


def displaytime(win, time):
    win.time_label.setText("Время: {0:.3f}msc".format(time))
    return


def activate_pixel(win, p, x, cur_y):
    if QColor(win.image.pixel(x, cur_y)) == bg_color:
        p.setPen(QPen(pen_color))
    else:
        p.setPen(QPen(bg_color))


def fill_polygon(win):
    t = QTime()
    pix = QPixmap()
    p = QPainter()

    t.start()
    xm = int(find_max_x(win.edges))
    p.begin(win.image)

    for ed in win.edges:
        x1, y1 = ed[0], ed[1]
        x2, y2 = ed[2], ed[3]

        if y1 == y2:
            continue

        if y1 > y2:
            y1, y2 = y2, y1
            x1, x2 = x2, x1

        cur_y = y1
        end_y = y2
        dx = (x2 - x1) / (y2 - y1)
        start_x = x1

        while cur_y < end_y:
            x = start_x
            while x < xm:
                activate_pixel(win, p, x, cur_y)
                p.drawPoint(x, cur_y)
                x += 1

            start_x += dx
            cur_y += 1
            if win.delay.isChecked():
                delay(win, pix)

        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)

    p.end()
    displaytime(win, t.elapsed())
    draw_edges(win.image, win.edges)


def add_point_by_btn(win):
    p = QPoint()

    p.setX(win.x.value())
    p.setY(win.y.value())

    add_point(p)


if __name__ == "__main__":
    pen_color = Qt.black
    bg_color = Qt.white

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
