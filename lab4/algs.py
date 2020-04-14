from math import sqrt, pi, sin, cos

def plotcircle(win, cx, x, cy, y):
    win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
    win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
    win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
    win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
    win.image.setPixel(cy + y, cx + x, win.pen.color().rgb())
    win.image.setPixel(cy + y, cx - x, win.pen.color().rgb())
    win.image.setPixel(cy - y, cx + x, win.pen.color().rgb())
    win.image.setPixel(cy - y, cx - x, win.pen.color().rgb())
    return

def plotellipse(win, cx, x, cy, y):
    win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
    win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
    win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
    win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
    return

def draw_brez(win, cx, cy, a, b):
    x = 0
    y = b
    a = a ** 2
    d = round(b * b / 2 - a * b * 2 + a / 2)
    b = b ** 2

    plotellipse(win, cx, x, cy, y)

    while y > 0:

        if d <= 0:
            buf = 2 * d + 2 * a * y - a
            x += 1
            if buf <= 0:
                d = d + 2 * b * x + b
            else:
                y -= 1
                d = d + 2 * b * x - 2 * a * y + a + b

        else:
            buf = 2 * d - 2 * b * x - b
            y -= 1

            if buf >= 0:  # вертикальный шаг
                d = d - 2 * y * a + a
            else:
                d = d + 2 * x * b - 2 * y * a + a + b
                x += 1

        plotellipse(win, cx, x, cy, y)



def draw_middle(win, cx, cy, a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b
    ad = 2 * a2
    bd = 2 * b2

    mid = a2 / sqrt(a2 + b2)
    f = b2 - a2 * b + 0.25 * a2
    dx = 0
    dy = -ad * y
    while x <= mid:
        plotellipse(win, cx, x, cy, y)

        if f > 0:
            y -= 1
            dy += ad
            f += dy
        x += 1
        dx += bd
        f += dx + b2

    f += -b2 * (x + 0.75) - a2 * (y - 0.75)

    while y >= 0:
        plotellipse(win, cx, x, cy, y)

        if f <= 0:
            x += 1
            dx += bd
            f += dx
        y -= 1
        dy += ad
        f += a2 + dy


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
    for x in range(0, r + 1 // 2 + 1, 1):
        y = round(sqrt(r ** 2 - x ** 2))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cy + y, cx + x, win.pen.color().rgb())
        win.image.setPixel(cy + y, cx - x, win.pen.color().rgb())
        win.image.setPixel(cy - y, cx + x, win.pen.color().rgb())
        win.image.setPixel(cy - y, cx - x, win.pen.color().rgb())

def circle_param(win, cx, cy, r):
    l = round(pi * r / 2 ) // 2
    for i in range(0, l + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))
        win.image.setPixel(cx + x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx + x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy + y, win.pen.color().rgb())
        win.image.setPixel(cx - x, cy - y, win.pen.color().rgb())
        win.image.setPixel(cy + y, cx + x, win.pen.color().rgb())
        win.image.setPixel(cy + y, cx - x, win.pen.color().rgb())
        win.image.setPixel(cy - y, cx + x, win.pen.color().rgb())
        win.image.setPixel(cy - y, cx - x, win.pen.color().rgb())


def circle_brez(win, cx, cy, r):
    x = 0
    y = r
    d = 2 - 2 * r
    plotcircle(win, cx, x, cy, y)
    while y >= x:

        if d <= 0:
            buf = 2 * d + 2 * y - 1
            x += 1
            if buf <= 0:
                d = d + 2 * x + 1
            else:
                d = d + 2 * x - 2 * y + 2
                y -= 1

        else:
            buf = 2 * d - 2 * x - 1
            y -= 1

            if buf >= 0:
                d = d - 2 * y + 1
            else:
                d = d + 2 * x - 2 * y + 2
                x += 1

        plotcircle(win, cx, x, cy, y)


def circle_middle(win, cx, cy, r):
    x = 0
    y = r
    d = 5 / 4 - r
    while x <= y:
        plotcircle(win, cx, x, cy, y)

        x += 1

        if d < 0:
            d += 2 * x + 1
        else:
            d += 2 * x - 2 * y + 5
            y -= 1
