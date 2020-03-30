from tkinter import *
import utilities as ut
import buttons as b
import matplotlib as mpl
import tkinter.messagebox as mb

def get_input(union1, union2):
    f = open("input.txt", 'r')
    un = union1
    for line in f:
        row = line.split(" ")
        if (len(row) != 2):
            un = union2
        else:
            oneDot = [float(row[0]), float(row[1])]
            if ut.check(oneDot[0]) == 0 and ut.check(oneDot[1]) == 0:
                un.append(oneDot)


def addDot(list1, list2):
    addWin = Tk()
    addWin.title("Добавление Точки")
    addWin.geometry('200x100+660+100')

    frameAdd = Frame(addWin)
    frameAdd.grid(row=0, column=0)

    xEntry = Entry(frameAdd, width=10)
    yEntry = Entry(frameAdd, width=10)

    runButton1 = Button(frameAdd, width=10, text="<- Розовая",
                       command=lambda: b.addButton(list1, xEntry, yEntry))

    runButton2 = Button(frameAdd, width=10, text="Голубая ->",
                       command=lambda: b.addButton(list2, xEntry, yEntry))

    backButton = Button(frameAdd, width=10, text="Назад",
                        command=lambda: addWin.destroy())

    xLabel = Label(frameAdd, width=10, text="X:")
    yLabel = Label(frameAdd, width=10, text="Y:")

    xEntry.grid(row=1, column=0)
    yEntry.grid(row=1, column=1)
    xLabel.grid(row=0, column=0)
    yLabel.grid(row=0, column=1)
    runButton1.grid(row=2, column=0)
    runButton2.grid(row=2, column=1)
    backButton.grid(row=3, column=0)

    list1.insert(list1.size() - 1)

    addWin.mainloop()


def editDot(list1):
    editWin = Tk()
    editWin.title("Редактирование Точки")
    editWin.geometry('200x90+660+100')

    frameAdd = Frame(editWin)
    frameAdd.grid(row=0, column=0)

    xnewEntry = Entry(frameAdd, width=10)
    ynewEntry = Entry(frameAdd, width=10)

    runButton = Button(frameAdd, width=10, text="Изменить",
                       command=lambda: b.editButton(list1, xnewEntry, ynewEntry, editWin))

    backButton = Button(frameAdd, width=10, text="Назад",
                        command=lambda: editWin.destroy())

    xnewLabel = Label(frameAdd, width=10, text="Новый X:")
    ynewLabel = Label(frameAdd, width=10, text="Новый Y:")

    xnewEntry.grid(row=3, column=0)
    ynewEntry.grid(row=3, column=1)
    xnewLabel.grid(row=2, column=0)
    ynewLabel.grid(row=2, column=1)
    runButton.grid(row=4, column=0)
    backButton.grid(row=4, column=1)

    list1.insert(list1.size() - 1)

    editWin.mainloop()


def print_ovals(c, dots, mx, my, colorp, colorb):
    for i in range(len(dots)):
        left = dots[i][0]    #точка: [[x, y], радиус]
        right = dots[i][1]
        x1 = left[0][0]
        y1 = left[0][1]
        r1 = left[1]
        x2 = right[0][0]
        y2 = right[0][1]
        r2 = right[1]

        c.create_oval(274 + mx * x1 - mx * r1, 274 - my * y1 - my * r1,
                    274 + mx * x1 + mx * r1, 274 - my * y1 + my * r1, outline=colorp)

        c.create_oval(274 + mx * x2 - mx * r2, 274 - my * y2 - my * r2,
                      274 + mx * x2 + mx * r2, 274 - my * y2 + my * r2, outline=colorb)

        c.create_oval(274 + mx * x1 - 2, 274 - my * y1 - 2,
                      274 + mx * x1 + 2, 274 - my * y1 + 2, fill="green", outline="green")

        c.create_text(274 + mx * x1 + 15, 274 - my * y1 - 15, text=[x1, y1], fill="green")

        c.create_oval(274 + mx * x2 - 2, 274 - my * y2 - 2,
                      274 + mx * x2 + 2, 274 - my * y2 + 2, fill="green", outline="green")

        c.create_text(274 + mx * x2 + 15, 274 - my * y2 - 15, text=[x2, y2], fill="green")
        if x1 < x2:     #если первый левее второго
            c.create_line(274 + mx * (x1 + r1), 274 - my * y1,
                          274 + mx * (x2 - r2), 274 - my * y2, fill="green")
        else:
            c.create_line(274 + mx * (x1 - r1), 274 - my * y1,
                          274 + mx * (x2 + r2), 274 - my * y2, fill="green")

def draw_dots(c, dots, mx, my, color):
    for dot in dots:
        print(dot)
        x1 = dot[0][0]
        y1 = dot[0][1]
        x2 = dot[1][0]
        y2 = dot[1][1]
        x3 = dot[2][0]
        y3 = dot[2][1]
        c.create_oval(274 + mx * x1 - 2, 274 - my * y1 - 2,
                      274 + mx * x1 + 2, 274 - my * y1 + 2, fill=color)
        c.create_oval(274 + mx * x2 - 2, 274 - my * y2 - 2,
                      274 + mx * x2 + 2, 274 - my * y2 + 2, fill=color)
        c.create_oval(274 + mx * x3 - 2, 274 - my * y3 - 2,
                      274 + mx * x3 + 2, 274 - my * y3 + 2, fill=color)
        c.create_text(274 + mx * x1 + 25, 274 - my * y1 - 25, text=[x1, y1])
        c.create_text(274 + mx * x2 + 25, 274 - my * y2 - 25, text=[x2, y2])
        c.create_text(274 + mx * x3 + 25, 274 - my * y3 - 25, text=[x3, y3])


def runWin(pinkdots, parr, barr):
    runWin = Tk()
    runWin.title("Результат")
    runWin.geometry('548x500+480+210')

    frameAdd = Frame(runWin)
    frameAdd.grid(row=0, column=0)

    c = Canvas(frameAdd, width=548, height=500)

    c.grid(row=0, column=0)
    rng = ut.find_range(pinkdots)
    #rngb = ut.find_range(bluedots)
    #rng = max(rngp)

    mx = 274 / (abs(rng[0]) + abs(rng[1]) + 1)
    my = 274 / (abs(rng[2]) + abs(rng[3]) + 1)

    mx, my = min(mx, my), min(mx,my)

    c.create_line(274, 0, 274, 548)
    c.create_line(0, 274, 548, 274)

    print_ovals(c, pinkdots, mx, my, "#ff00ff", "blue")
    #print_ovals(c, bluedots, mx, my, "blue")
    draw_dots(c, parr, mx, my, "green")
    draw_dots(c, barr, mx, my, "blue")
    messageWin(pinkdots)

def messageWin(dots):
    msgWin = Tk()
    msgWin.title("Список окружностей:")
    msgWin.geometry('280x400+1050+210')

    frame = Frame(msgWin)
    frame.grid(row=0, column=0)
    list1 = Listbox(frame, bg="#fce8ff", height=60, width=15)
    list2 = Listbox(frame, bg="#e8eeff", height=60, width=15)

    list1.grid(row=0, column=0)
    list2.grid(row=0, column=1)

    for i in range(2, len(dots) - 1):
        left = dots[i][0]    #точка: [[x, y], радиус]
        right = dots[i][1]
        x1 = left[0][0]
        y1 = left[0][1]
        r1 = left[1]
        x2 = right[0][0]
        y2 = right[0][1]
        r2 = right[1]

        x = "x центра = ", x1
        y = "y центра = ", y1
        r = "Радиус = ", r1
        list1.insert(0, "====================")
        list1.insert(0, x)
        list1.insert(0, y)
        list1.insert(0, r)
        list2.insert(0, "====================")
        x = "x центра = ", x2
        y = "y центра = ", y2
        r = "Радиус = ", r2
        list2.insert(0, x)
        list2.insert(0, y)
        list2.insert(0, r)


