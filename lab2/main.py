# Тема: Работа с изображениями                                               #
# Программа выполняет поворот, перемещение и масштаб                         #
# ========================================================================== #
# Входные данные:        Результат:                                          #
# Параметры изменений    Измененное изображение                              #

from tkinter import *
from tkinter import messagebox as mb
import drawing as dr
import user_interface as ui

center = [300, 300]
move = [300, 300]
turn = [300, 300, 0]
scale = [300, 300, 1, 1]

if __name__ == '__main__':
    root = Tk()
    root.title("Танк")
    root.geometry("800x600+300+100")

    btnFrame = Frame(height=600, width=200, bg="white")
    cnvFrame = Frame(height=600, width=600, bg="#fcf9fe")

    c = Canvas(cnvFrame, heigh=600, width=600, bg="#fcf9fe")

    c.grid(row=0, column=0)

    titleLabel = Label(btnFrame, text="ГЛАВНОЕ МЕНЮ")
    emptyLabel = Label(btnFrame, heigh=2)
    emptyLabel2 = Label(btnFrame, heigh=2)
    emptyLabel3 = Label(btnFrame, heigh=2)
    emptyLabel4 = Label(btnFrame, heigh=2)

    btnFrame.grid(row=0, column=0)
    cnvFrame.grid(row=0, column=1)

    titleLabel.grid(row=0,column=0)
    emptyLabel.grid(row=1, column=0)
    emptyLabel2.grid(row=4, column=0)
    emptyLabel3.grid(row=7, column=0)
    emptyLabel4.grid(row=10, column=0)

    moveLabel = Label(btnFrame, text="ПЕРЕНОС")

    moveLabel.grid(row=2, column=0)

    moveFrame = Frame(btnFrame, height=10, width=200)
    moveOxEntry = Entry(moveFrame, width=3)
    moveOxEntry.insert(0, "300")
    moveOyEntry = Entry(moveFrame, width=3)
    moveOyEntry.insert(0, "300")
    moveOxLabel = Label(moveFrame, text="Ox", width=3)
    moveOyLabel = Label(moveFrame, text="Oy", width=3)

    moveFrame.grid(row=3, column=0)
    moveOxEntry.grid(row=0, column=0)
    moveOyEntry.grid(row=0, column=1)
    moveOxLabel.grid(row=1, column=0)
    moveOyLabel.grid(row=1, column=1)

    turnLabel = Label(btnFrame, text="ПОВОРОТ")

    turnLabel.grid(row=5, column=0)

    turnFrame = Frame(btnFrame, height=10, width=200)
    turnOxEntry = Entry(turnFrame, width=3)
    turnOxEntry.insert(0, "300")
    turnOyEntry = Entry(turnFrame, width=3)
    turnOyEntry.insert(0, "300")
    turnAngleEntry = Entry(turnFrame, width=3)
    turnAngleEntry.insert(0, "0")
    turnOxLabel = Label(turnFrame, text="Ox", width=3)
    turnOyLabel = Label(turnFrame, text="Oy", width=3)
    turnAngleLabel = Label(turnFrame, text="Угол", width=3)

    turnFrame.grid(row=6, column=0)
    turnOxEntry.grid(row=0, column=0)
    turnOyEntry.grid(row=0, column=1)
    turnOxLabel.grid(row=1, column=0)
    turnOyLabel.grid(row=1, column=1)
    turnAngleEntry.grid(row=0, column=2)
    turnAngleLabel.grid(row=1, column=2)

    scaleLabel = Label(btnFrame, text="МАСШТАБ")

    scaleLabel.grid(row=8, column=0)

    scaleFrame = Frame(btnFrame, height=10, width=200)
    scaleOxEntry = Entry(scaleFrame, width=3)
    scaleOxEntry.insert(0, "300")
    scaleOyEntry = Entry(scaleFrame, width=3)
    scaleOyEntry.insert(0, "300")
    scaleKxEntry = Entry(scaleFrame, width=3)
    scaleKxEntry.insert(0, "1")
    scaleKyEntry = Entry(scaleFrame, width=3)
    scaleKyEntry.insert(0, "1")
    scaleOxLabel = Label(scaleFrame, text="Ox", width=3)
    scaleOyLabel = Label(scaleFrame, text="Oy", width=3)
    scaleKxLabel = Label(scaleFrame, text="Kx", width=3)
    scaleKyLabel = Label(scaleFrame, text="Kx", width=3)


    scaleFrame.grid(row=9, column=0)
    scaleOxEntry.grid(row=0, column=0)
    scaleOyEntry.grid(row=0, column=1)
    scaleOxLabel.grid(row=1, column=0)
    scaleOyLabel.grid(row=1, column=1)
    scaleKxEntry.grid(row=0, column=2)
    scaleKxLabel.grid(row=1, column=2)
    scaleKyEntry.grid(row=0, column=3)
    scaleKyLabel.grid(row=1, column=3)

    moveEnts = [moveOxEntry, moveOyEntry]
    turnEnts = [turnOxEntry, turnOyEntry, turnAngleEntry]
    scaleEnts = [scaleOxEntry, scaleOyEntry, scaleKxEntry, scaleKyEntry]

    runButton = Button(btnFrame, text="РЕЗУЛЬТАТ",
                       command=lambda:ui.mainButton(moveEnts, turnEnts, scaleEnts, c))
    runButton.grid(row=11, column=0)

    backButton = Button(btnFrame, text="ОТМЕНА")
    backButton.grid(row=12, column=0)

    dr.getpicture(c, move, turn, scale)
    root.mainloop()
