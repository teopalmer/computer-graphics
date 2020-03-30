# Тема: Множества точек                                                      #
# Программа находит и изображает нек. кол-во окружностей                     #
# ========================================================================== #
# Входные данные:        Результат:                                          #
# Два множества точек    Найти и изобразить графически все пары окружностей, #
#                        каждая из которых проходит минимум через три        #
#                        различные точки одного множества таких, что         #
#                        касательная к обеим окружностям параллельна Ох      #

from tkinter import *
import matplotlib
import tkinter.messagebox as mb
import user_interface as ui
matplotlib.use("TkAgg")
import buttons as b

if __name__ == '__main__':
    root = Tk()
    root.title("Множество точек")
    root.geometry('507x300+500+50')

    frame = Frame(root)
    frame.grid(row=1, column=0)
    buttons = Frame(frame)
    buttons.grid(row=0, column=1)

    listLabel1 = Label(frame, text="Розовые точки")
    listLabel2 = Label(frame, text="Голубые точки")

    list1 = Listbox(frame, bg="#fce8ff")
    list2 = Listbox(frame, bg="#e8eeff")

    list1.grid(row=0, column=0)
    listLabel1.grid(row=1, column=0)
    list2.grid(row=0, column=2)
    listLabel2.grid(row=1, column=2)

    fileButton = Button(buttons, text="Ввод Из Файла", width=15,
                        command=lambda: b.fileInput(list1, list2))

    addButton = Button(buttons, text="Добавить Точку", width=15,
                       command=lambda: ui.addDot(list1, list2))

    delButton1 = Button(frame, text="Удалить Розовую Точку", width=20,
                       command=lambda: b.deleteButton(list1))

    delButton2 = Button(frame, text="Удалить Голубую Точку", width=20,
                        command=lambda: b.deleteButton(list2))

    editButton1 = Button(frame, text="Изменить Розовую Точку", width=20,
                        command=lambda: ui.editDot(list1))

    editButton2 = Button(frame, text="Изменить Голубую Точку", width=20,
                         command=lambda: ui.editDot(list2))
    clearallButton = Button(buttons, text="Очистить все", width=15,
                            command=lambda: b.clearAll(list1, list2))

    runButton = Button(buttons, text="Запуск", width=15, fg='green',
                       command=lambda: b.runButton(list1, list2))

    fileButton.grid(row=0, column=1)
    addButton.grid(row=1, column=1)
    delButton1.grid(row=2, column=0)
    delButton2.grid(row=2, column=2)
    editButton1.grid(row=3, column=0)
    editButton2.grid(row=3, column=2)
    clearallButton.grid(row=6, column=1)
    runButton.grid(row=7, column=1)

    root.mainloop()
