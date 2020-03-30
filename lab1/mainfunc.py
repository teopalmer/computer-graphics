import math
import itertools as it

eps = 0.0001
def distance_between_points(xy1, xy2):
    x_1 = xy1[0]
    x_2 = xy2[0]
    y_1 = xy1[1]
    y_2 = xy2[1]
    dis = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dis

def find_cir(p1, p2, p3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    if x1 == x2 == x3:
        return None
    if x2 == x1:
        x2, x3 = x3, x2
        y2, y3 = y3, y2
    elif x2 == x3:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    ma = (y2 - y1) / (x2 - x1)
    mb = (y3 - y2) / (x3 - x2)
    if ma != mb:
        x_centre = (ma * mb * (y1 - y3) + mb * (x1 + x2) - ma * (x2 + x3)) / (2 * (mb - ma))
        if ma == 0:
            y_centre = (-1 / mb) * (x_centre - (x2 + x3) / 2) + ((y2 + y3) / 2)
        else:
            y_centre = (-1 / ma) * (x_centre - (x1 + x2) / 2) + ((y1 + y2) / 2)
        radius = distance_between_points([x_centre, y_centre], [x1, y1])
        return [[x_centre, y_centre], radius]
    else:
        return None

def is_true(c1, c2, r1, r2):
    test1ca = c1 + r1
    test1cb = c2 - r2
    test2ca = c1 - r1
    test2cb = c2 + r2

    if abs(test1ca - test1cb) <= eps or abs(test2ca - test2cb) <= eps:
        return 1
    else:
        return 0

def equate_circ(cir1, cir2, clist):
    if cir1 != None and cir2 != None:
        if is_true(cir1[0][0], cir2[0][0], cir1[1], cir2[1]) == 1:
            clist.append([cir1, cir2])
            return 1
        else:
            return 0


def check_all(list1, list2):
    clist = []
    dotpinks = []
    dotblues= []
    for x in it.combinations(list1, 3):
        fa, fb, fc = x[0], x[1], x[2]
        for y in it.combinations(list2, 3):
            sa, sb, sc = y[0], y[1], y[2]
            cir1 = find_cir(fa, fb, fc)
            cir2 = find_cir(sa, sb, sc)
            if equate_circ(cir1, cir2, clist) == 1:
                dotpinks.append([fa, fb, fc])
                dotblues.append([sa, sb, sc])

    return clist, dotpinks, dotblues
