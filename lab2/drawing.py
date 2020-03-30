from tkinter import *
import math as m
import utilities as ut
bgcolor = "#fcf9fe"

sidearcs = [130, 70, 30]
upperarc = [80, 100, 20, 30]
mainbody = [100, 30]
upperbody = [70, 30, 80]
tube = [30, 97, 10]

def calc_turn(dot, turn, center):
    angle = turn[2]*(3.14/180)
    dot = ut.new_coord_turn(dot, center, turn)
    x1 = dot[0] * m.cos(angle) - dot[1] * m.sin(angle)
    y1 = dot[0] * m.sin(angle) + dot[1] * m.cos(angle)
    print("New dot", x1, y1)
    return x1, y1

def deform(x, move, turn, scale):
    return 0

def draw_window(c, center, xm, turn):
    dot1 = [center[0] - xm, center[1] + xm]
    dot2 = [center[0] + xm, center[1] - xm]
    dot1 = calc_turn(dot1, turn, center)
    dot2 = calc_turn(dot2, turn, center)

    print("Dots:", dot1, dot2)
    c.create_arc(dot1, dot2,
                 start=0, extent=359, outline="Black", style=ARC, fill="Black")

def draw_mainbody(c, center, xm, ym):

    c.create_line(center[0] + xm, center[1] + ym,
                  center[0] - xm, center[1] + ym, fill="Black")
    c.create_line(center[0] + xm, center[1] - ym,
                  center[0] - xm, center[1] - ym, fill="Black")

def draw_upperbody(c, center, xm, ymu, ymd):

    c.create_line(center[0] + xm, center[1] - ymu,
                  center[0] + xm, center[1] - ymd, fill="Black")
    c.create_line(center[0] - xm, center[1] - ymu,
                  center[0] - xm, center[1] - ymd, fill="Black")
    c.create_line(center[0] - xm, center[1] - ymd,
                  center[0] + xm, center[1] - ymd, fill="Black")

def draw_sidearcs(c, center, xmu, xmd, ym):

    c.create_arc(center[0] + xmu, center[1] + ym,
                 center[0] + xmd, center[1] - ym,
                 start=270, extent=180, style=ARC, outline="Black")
    c.create_arc(center[0] - xmu, center[1] + ym,
                 center[0] - xmd, center[1] - ym,
                 start=90, extent=180, style=ARC, outline="Black")



def draw_upperarc(c, center, xm, ymu, ymd, angle):

    c.create_arc(center[0] + xm, center[1] - ymu,
               center[0] - xm, center[1] - ymd,
               start=angle, extent=120, style=ARC, outline="Black")


def draw_tube(c, center, xm, ym, step):
    xml = xm - step * 2 #left x
    xmc = xm - step   #center x
    ymu = ym + step * 2 #left y
    ymc = ym + step     #center y

    c.create_line(center[0] - xm, center[1] - ym,
               center[0] - xm, center[1] - ymu,
               center[0] - xml, center[1] - ymu,
               center[0] - xml, center[1] - ymc,
               center[0] - xmc, center[1] - ymc,
               center[0] - xmc, center[1] - ym - 1,
               fill="black")
    return 0

def deform_x(x, move, turn, scale, tag):    #tag = x/y
    return 0

def getpicture(c, center, turn, scale):

    draw_sidearcs(c, center, 130, 70, 30)

    draw_upperarc(c, center, 80, 100, 20, 30)

    draw_mainbody(c, center, 100, 30)

    draw_upperbody(c, center, 70, 30, 80)

    draw_tube(c, center, 30, 97, 10)

    draw_window(c, center, 10, turn)
    #draw_window(c, [center[0] - 40, center[1]], 10, 10)
    #draw_window(c, [center[0] - 80, center[1]], 10, 10)
    #draw_window(c, [center[0] + 40, center[1]], 10, 10)
    #draw_window(c, [center[0] + 80, center[1]], 10, 10)
    return center
