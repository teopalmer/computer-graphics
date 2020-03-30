from tkinter import *
import main
import tkinter.messagebox as mb

def find_range(clist):
    ymax = -999
    ymin = 999
    xmax = -999
    xmin = 999
    for i in range(0, len(clist)):
        left = clist[i][0]
        right = clist[i][1]
        nowmax = max(left[0][1] + left[1], right[0][1] + right[1])
        nowmin = min(left[0][1] - left[1], right[0][1] - right[1])
        if nowmax > ymax:
            ymax = nowmax
        if nowmin < ymin:
            ymin = nowmin
    for i in range(0, len(clist)):
        left = clist[i][0]
        right = clist[i][1]
        nowmax = max(left[0][0] + left[1], right[0][0] + right[1])
        nowmin = min(left[0][0] - left[1], right[0][0] - right[1])
        if nowmax > xmax:
            xmax = nowmax
        if nowmin < xmin:
            xmin = nowmin

    return xmax, xmin, ymax, ymin

def find_x_range(clist):
    xmax = 999
    xmin = -999
    for i in range(len(clist)):
        left = clist[i][0]
        right = clist[i][1]
        nowmax = max(left[1][1] + left[1], right[1][1] + right[1])
        nowmin = min(left[1][1] - left[1], right[1][1] - right[1])
        if nowmax > xmax:
            ymax = nowmax
        if nowmin < xmin:
            ymin = nowmin

def clear_list(list1):
    size = list1.size()
    list1.delete(0, size)

def check(input):
    try:
        input = float(input)
    except ValueError:
        mb.showerror("ОШИБКА ВВОДА", "Неверный ввод")
        return 1
    return 0

def isIn(lis, x, y):
    l = lis.get(0, END)
    try:
        l.index((float(x), float(y)))
        mb.showerror("ОШИБКА", "Такая точка уже существует")
        return 1
    except ValueError:
        return 0
