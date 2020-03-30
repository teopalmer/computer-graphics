from tkinter import *
from tkinter import messagebox as mb
import drawing as dr

move = [300, 300]
turn = [300, 300, 0]
scale = [300, 300, 1, 1]

def get_move(entries):
    try:
        moveX = float(entries[0].get())
        moveY = float(entries[1].get())
    except ValueError:
        mb.showerror("ОШИБКА", "Неверный ввод параметров переноса")
        return None, None
    return moveX, moveY

def get_turn(entries):
    try:
        moveX = float(entries[0].get())
        moveY = float(entries[1].get())
        angle = float(entries[2].get())
    except ValueError:
        mb.showerror("ОШИБКА", "Неверный ввод параметров поворота")
        return None, None, None
    return moveX, moveY, angle

def get_scale(entries):
    try:
        moveX = float(entries[0].get())
        moveY = float(entries[1].get())
        kX = float(entries[2].get())
        kY = float(entries[3].get())
    except ValueError:
        mb.showerror("ОШИБКА", "Неверный ввод параметров масштаба")
        return None, None, None, None
    return moveX, moveY, kX, kY

def mainButton(moveEntries, turnEntries, scaleEntries, c):
    center = [300, 300]
    global move, turn, scale
    move[0] = get_move(moveEntries)[0]
    move[1] = get_move(moveEntries)[1]

    turn[0] = get_turn(turnEntries)[0]
    turn[1] = get_turn(turnEntries)[1]
    turn[2] += get_turn(turnEntries)[2]

    scale[0] = get_scale(scaleEntries)[0]
    scale[1] = get_scale(scaleEntries)[1]
    scale[2] += get_scale(scaleEntries)[2]
    scale[3] += get_scale(scaleEntries)[3]

    if (move[0] != None and turn[0] != None and scale[0] != None):
        c.delete("all")
        dr.getpicture(c, move, turn, scale)

