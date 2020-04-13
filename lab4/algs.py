from math import sqrt, pi, sin, cos

def draw_brez(win, cx, cy, a, b):
    x = 0  # начальные значения
    y = b
    a = a ** 2
    d = round(b * b / 2 - a * b * 2 + a / 2)
    b = b ** 2
    while y >= 0:
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        if d < 0:  # пиксель лежит внутри эллипса
            buf = 2 * d + 2 * a * y - a
            x += 1
            if buf <= 0:  # горизотальный шаг
                d = d + 2 * b * x + b
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * b * x - 2 * a * y + a + b

            continue

        if d > 0:  # пиксель лежит вне эллипса
            buf = 2 * d - 2 * b * x - b
            y -= 1

            if buf > 0:  # вертикальный шаг
                d = d - 2 * y * a + a
            else:  # диагональный шаг
                x += 1
                d = d + 2 * x * b - 2 * y * a + a + b

            continue

        if d == 0.0:  # пиксель лежит на окружности
            x += 1  # диагональный шаг
            y -= 1
            d = d + 2 * x * b - 2 * y * a + a + b
    return


def draw_middle(win, cx, cy, a, b):
    x = 0  # начальные положения
    y = b
    p = b * b - a * a * b + 0.25 * a * a  # начальное значение параметра принятия решения в области tg<1
    while 2 * (b ** 2) * x < 2 * a * a * y:  # пока тангенс угла наклона меньше 1
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())

        x += 1

        if p < 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
            p += 2 * b * b * x + b * b
        else:  # средняя точка вне эллипса, ближе диагональный пиксел, диагональный шаг
            y -= 1
            p += 2 * b * b * x - 2 * a * a * y + b * b

    p = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения

    while y >= 0:
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())

        y -= 1

        if p > 0:
            p -= 2 * a * a * y + a * a
        else:
            x += 1
            p += 2 * b * b * x - 2 * a * a * y + a * a
    return


def draw_canon(win, cx, cy, a, b):
    for x in range(0, a + 1, 1):
        y = round(b * sqrt(1.0 - x ** 2 / a / a))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())

    for y in range(0, b + 1, 1):
        x = round(a * sqrt(1.0 - y ** 2 / b / b))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
    return


def draw_param(win, cx, cy,  a, b):
    m = max(a, b)
    l = round(pi * m / 2)
    for i in range(0, l + 1, 1):
        x = round(a * cos(i / m))
        y = round(b * sin(i / m))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
    return


def draw_lib(win, x, y, rx, ry):
    return

def circle_canon(win, cx, cy, r):
    for x in range(0, r + 1, 1):
        y = round(sqrt(r ** 2 - x ** 2))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())

    for y in range(0, r + 1, 1):
        x = round(sqrt(r ** 2 - y ** 2))

        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())

def circle_param(win, cx, cy, r):
    l = round(pi * r / 2 )  # длина четврети окружности
    for i in range(0, l + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())


def circle_brez(win, cx, cy, r):
    x = 0   # задание начальных значений
    y = r
    d = 2 - 2 * r   # значение D(x,y)  при (0,R)
    while y >= 0:
        # высвечивание текущего пиксела
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())

        if d < 0:  # пиксель лежит внутри окружности
            buf = 2 * d + 2 * y - 1
            x += 1

            if buf <= 0:  # горизонтальный шаг
                d = d + 2 * x + 1
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d > 0:  # пиксель лежит вне окружности
            buf = 2 * d - 2 * x - 1
            y -= 1

            if buf > 0:  # вертикальный шаг
                d = d - 2 * y + 1
            else:  # диагональный шаг
                x += 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d == 0.0:  # пиксель лежит на окружности
            x += 1   # диагональный шаг
            y -= 1
            d = d + 2 * x - 2 * y + 2


def circle_middle(win, cx, cy, r):
    x = 0  # начальные значения
    y = r
    p = 5 / 4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2
    while True:
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())

        win.image.setPixel(cx - y, cy + x, win.pen.color().rgb())
        win.image.setPixel(cx + y, cy - x, win.pen.color().rgb())
        win.image.setPixel(cx - y, cy - x, win.pen.color().rgb())
        win.image.setPixel(cx + y, cy + x, win.pen.color().rgb())

        x += 1

        if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
            p += 2 * x + 1
        else:   # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
            p += 2 * x - 2 * y + 5
            y -= 1

        if x > y:
            break
