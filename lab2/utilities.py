import math

def distance_between_points(xy1, xy2):
    x_1 = xy1[0]
    x_2 = xy2[0]
    y_1 = xy1[1]
    y_2 = xy2[1]
    dis = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dis

def new_coord_turn(xy, center, turn):
    x = xy[0]
    y = xy[1]
    cx = center[0]
    cy = center[1]
    tx = turn[0]
    ty = turn[1]
    xnew = cx - tx + x
    ynew = cy - tx + y
    return [xnew, ynew]

def get_coord_back(xy, center, turn):
    return 0
