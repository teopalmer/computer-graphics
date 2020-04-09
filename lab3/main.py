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
        self.draw_sun.clicked.connect(lambda: draw_sun(self))
        self.cda.setChecked(True)

def clear_all(win):
    win.image.fill(Qt.color0)
    win.scene.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
