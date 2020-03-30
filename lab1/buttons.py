from tkinter import *
import main
import tkinter.messagebox as mb

import matplotlib
import utilities as ut
import user_interface as ui
import mainfunc as mf
matplotlib.use("TkAgg")

def keyboard(key):
    if key == 'FileInput':
        return 2

def fileInput(list1, list2):
    union1 = []
    union2 = []
    ut.clear_list(list1)
    ut.clear_list(list2)
    ui.get_input(union1, union2)
    for i in (union1):
        list1.insert(0, i)
    for i in (union2):
        list2.insert(0, i)
    #for i in ("one", "two"):
        #list1.insert(0, i)

def addButton(list1, xEntry, yEntry):
    x = xEntry.get()
    y = yEntry.get()
    if ut.check(x) or ut.check(y):
        return 0
    if (ut.isIn(list1, x, y) == 1):
        return 0
    list1.insert(0, [float(x), float(y)])

def clearAll(list1, list2):
    ut.clear_list(list1)
    ut.clear_list(list2)

def deleteButton(list1):
    list1.delete(ANCHOR)

def editButton(list1, xnew, ynew, win):
    xn = xnew.get()
    yn = ynew.get()
    if ut.check(xn) == 1 or ut.check(yn) == 1:
        mb.showerror("ERROR", "Incorrect New Input")
    if ut.isIn(list1, xn, yn) == 0:
        xn = float(xn)
        yn = float(yn)
        list1.delete(ANCHOR)
        list1.insert(ANCHOR, [xn, yn])
    win.destroy()

def runButton(list1, list2):
    l1 = list1.get(0, END)
    l2 = list2.get(0, END)
    c = mf.check_all(l1, l2)
    print("*", c)
    #cblue = mf.check_all(l2)
    c1 = c[0]
    dp1 = c[1]
    db1 = c[2]
    ui.runWin(c1, dp1, db1)






