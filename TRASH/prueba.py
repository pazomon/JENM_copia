# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter
from Wanted_functions import yellow as wfy
from Settings import media

ca = media.sttingsmedia()


class Planificador(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("Tareas asignadas al rol Jefatura de Estudios")
        self.master.geometry('719x551')  # 415+4+200, 497+3*18
        self.master.configure(background=ca.colorinstitucional)
        self.frameOne = Frame(self.master)
        self.frameOne.grid(row=0, column=0)
        self.frameOne.configure(background=ca.colorinstitucional)

        self.frameTwo = Frame(self.master)
        self.frameTwo.grid(row=1, column=0)
        self.frameTwo.configure(background=ca.colorinstitucional)

        # Creating of a new frame, inside of "frameTwo" to the objects to be inserted
        # Creating a scrollbar

        # The reason for this, is to attach the scrollbar to "FrameTwo", and when the size of frame "ListFrame" exceed the size of frameTwo, the scrollbar acts
        self.canvas = Canvas(self.frameTwo)
        self.canvas.configure(background=ca.colorinstitucional, highlightbackground=ca.colorinstitucional)
        self.listFrame = Frame(self.canvas)
        self.scrollb = Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.scrollb.grid(row=1, column=0, sticky='nsew')  # grid scrollbar in master, but
        self.canvas['yscrollcommand'] = self.scrollb.set  # attach scrollbar to frameTwo

        self.canvas.create_window((0, 0), window=self.listFrame, anchor='nw')
        self.listFrame.bind("<Configure>", self.AuxscrollFunction)
        self.scrollb.grid_forget()  # Forget scrollbar because the number of pieces remains undefined by the user. But this not destroy it. It will be "remembered" later.

        self.canvas.pack(side="left")
        self.frameThree = Frame(self.master)
        self.frameThree.grid(row=2, column=0)

        self.button_instud = Button(self.frameOne, text="Introducir alumnos", width=20)
        self.button_instud.grid(row=3, column=0)

        self.button_insub = Button(self.frameOne, text="Introducir asignaturas", width=20)
        self.button_insub.grid(row=4, column=0)

        self.button_inmarks = Button(self.frameOne, text="Introducir notas", command=self.inmark, width=20)
        self.button_inmarks.grid(row=5, column=0)

        # self.aceptarnumpiezas = Button(self.frameOne,text="Click me", command=self.aceptar_piezas_ok,width=8)
        # self.aceptarnumpiezas.grid(row=6, column=0, pady=(5,5))

    def AuxscrollFunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=600, height=500)

    def inmark(self):
        self.button_im_single = Button(self.frameOne, text="Individual", width=20)
        self.button_im_single.grid(row=4, column=1)

        self.button_im_group = Button(self.frameOne, text="Grupal", command=self.img, width=20)
        self.button_im_group.grid(row=5, column=1)

        self.button_im_load = Button(self.frameOne, text="Carga de archivo", width=20)
        self.button_im_load.grid(row=6, column=1)

    def img(self):
        global ycl_desplegable, yellow_courses, yellow_curriculo_number, courses_list

        yellow_courses, yellow_curriculo_number, courses_list = wfy.courses()
        self.yc_list = tkinter.StringVar()
        ycl_desplegable = ttk.Combobox(self.frameOne, textvariable=self.yc_list, width=30)
        ycl_desplegable['values'] = courses_list
        ycl_desplegable.grid(row=5, column=2)
        self.button_yclsc = Button(self.frameOne, text="Seleccionar curso", command=self.img_subjects, width=20)
        self.button_yclsc.grid(row=5, column=3)

    def img_subjects(self):
        ycl_select = ycl_desplegable.get()

        for index, course in enumerate(courses_list):
            if ycl_select == course:
                yc_select = yellow_courses[index]
                ycn_select = yellow_curriculo_number[index]
        list_st = wfy.students(yc_select, ycn_select)
        self.num_piezas = len(list_st)

        self.scrollb.grid(row=1, column=1,
                          sticky='nsew')  # grid scrollbar in master, because user had defined the numer of pieces
        # self.aceptarnumpiezas.grid_remove()

        self.optionmenus_piezas = list()
        self.numpiezas = []
        self.numerolotes = []
        self.optionmenus_prioridad = list()
        self.lotes = list()

        self.mispiezas = ['One', 'Two', 'Three', 'Four', 'Five']

        self.n = 1
        while self.n <= int(self.num_piezas):
            self.textopieza = Label(self.listFrame, text=list_st[self.n - 1]['numero'], justify="left", width=20)
            self.textopieza.grid(row=self.n, column=0)
            self.numpiezastext = Label(self.listFrame, text=list_st[self.n - 1]['nombre'], justify="center", width=20)
            self.numpiezastext.grid(row=self.n, column=1, padx=(10, 0))

            self.entrynumpiezas = Entry(self.listFrame, width=20)
            self.entrynumpiezas.grid(row=self.n, column=2, padx=(0, 10))
            self.entrynumpiezas.insert(0, "0")

            self.entrynumpiezas2 = Entry(self.listFrame, width=20)
            self.entrynumpiezas2.grid(row=self.n, column=3, padx=(0, 10))
            self.entrynumpiezas2.insert(0, "0")

            self.var1 = IntVar()
            self.entrynumlotes = Checkbutton(self.listFrame, variable=self.var1)
            self.entrynumlotes.grid(row=self.n, column=7, padx=(5, 10))

            self.n += 1

        self.anadirpiezas = Button(self.frameThree, text="Add row", command=self.addpieza, width=10)
        self.anadirpiezas.grid(row=0, column=2, pady=(10, 10))

    def addpieza(self):
        print('hrllo')


if __name__ == "__main__":
    root = Tk()
    aplicacion = Planificador(root)
    root.mainloop()