# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter
from Wanted_functions import yellow as wfy
from Wanted_functions import student_plans as wfs
from Settings import media

ca = media.sttingsmedia()

class Planificador(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("Tareas asignadas al rol Jefatura de Estudios")
        self.master.geometry('1169x551')  # 415+4+500, 497+3*18
        self.master.configure(background=ca.colorinstitucional)
        self.frameOne = Frame(self.master)
        self.frameOne.grid(row=0,column=0)
        self.frameOne.configure(background=ca.colorinstitucional)

        self.frameTwo = Frame(self.master)
        self.frameTwo.grid(row=1, column=0)
        self.frameTwo.configure(background=ca.colorinstitucional)

        #Creating of a new frame, inside of "frameTwo" to the objects to be inserted
        #Creating a scrollbar

        #The reason for this, is to attach the scrollbar to "FrameTwo", and when the size of frame "ListFrame" exceed the size of frameTwo, the scrollbar acts
        self.canvas=Canvas(self.frameTwo)
        self.canvas.configure(background=ca.colorinstitucional, highlightbackground=ca.colorinstitucional)
        self.listFrame=Frame(self.canvas)
        self.scrollb=Scrollbar(self.master, orient="vertical",command=self.canvas.yview)
        self.scrollb.grid(row=1, column=0, sticky='nsew')  #grid scrollbar in master, but
        self.canvas['yscrollcommand'] = self.scrollb.set   #attach scrollbar to frameTwo

        self.canvas.create_window((0,0),window=self.listFrame,anchor='nw')
        self.listFrame.bind("<Configure>", self.AuxscrollFunction)
        self.listFrame.configure(background=ca.colorinstitucional)
        self.scrollb.grid_forget()                         #Forget scrollbar because the number of pieces remains undefined by the user. But this not destroy it. It will be "remembered" later.

        self.canvas.pack(side="left")
        self.frameThree = Frame(self.master)
        self.frameThree.grid(row=2, column=0)

        self.button_instud = Button(self.frameOne, text="Introducir alumnos", width=21)
        self.button_instud.grid(row=3, column=0)

        self.button_insub = Button(self.frameOne, text="Introducir asignaturas", width=21)
        self.button_insub.grid(row=4, column=0)

        self.button_inmarks = Button(self.frameOne, text="Introducir notas", command=self.inmark, width=21)
        self.button_inmarks.grid(row=5, column=0)

        #self.aceptarnumpiezas = Button(self.frameOne,text="Click me", command=self.aceptar_piezas_ok,width=8)
        #self.aceptarnumpiezas.grid(row=6, column=0, pady=(5,5))

    def AuxscrollFunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=1150,height=400)

    def inmark(self):
        self.button_im_single = Button(self.frameOne, text="Individual", width=50)
        self.button_im_single.grid(row=4, column=1)

        self.button_im_group = Button(self.frameOne, text="Grupal", command=self.img, width=50)
        self.button_im_group.grid(row=5, column=1)

        self.button_im_load = Button(self.frameOne, text="Carga de archivo", width=50)
        self.button_im_load.grid(row=6, column=1)

    def img(self):
        global ycl_desplegable, yellow_courses, yellow_curriculo_number, courses_list

        yellow_courses, yellow_curriculo_number, courses_list = wfy.courses()
        self.yc_list = tkinter.StringVar()
        ycl_desplegable = ttk.Combobox(self.frameOne, textvariable=self.yc_list, width=30)
        ycl_desplegable['values'] = courses_list
        ycl_desplegable.grid(row=5, column=2)
        self.button_yclsc = Button(self.frameOne, text="Seleccionar curso", command=self.img_subjects, width=21)
        self.button_yclsc.grid(row=5, column=3)

    def img_subjects(self):
        global ycl_desplegable2, selection

        selection = ycl_desplegable.get()

        for index, select_course in enumerate (courses_list):
            if select_course == selection:
                #course = yellow_courses[index]
                number_curr = yellow_curriculo_number[index]
                break
        courses_list2 = wfs.sujects(number_curr)
        self.yc_list2= "TODO leer asignatura de curso en plan de estudios"
        ycl_desplegable2 = ttk.Combobox(self.frameOne, textvariable=self.yc_list2, width=30)
        ycl_desplegable2['values'] = courses_list2
        ycl_desplegable2.grid(row=6, column=2)
        self.button_yclsc2 = Button(self.frameOne, text="Seleccionar asignatura", command=self.img_marks, width=21)
        self.button_yclsc2.grid(row=6, column=3)

    def img_marks(self):
        ycl_select = ycl_desplegable2.get()

        mark_perc = IntVar
        mark_perc_acc = IntVar
        mark_perc_lab = ttk.Label(self.frameOne, text='Avance evaluación', justify="left", width=21)
        mark_perc_lab.grid(row=7, column=0)
        mark_perc_ent = Entry(self.frameOne, textvariable=mark_perc, width=50)
        mark_perc_ent.grid(row=7, column=1)
        mark_perc_lab_acc = Label(self.frameOne, text='Avance asignatura', width=30)
        mark_perc_lab_acc.grid(row=7, column=2)
        mark_perc_ent_acc = Entry(self.frameOne, textvariable=mark_perc_acc, width=21)
        mark_perc_ent_acc.grid(row=7, column=3)

        #col_vac=Label(self.frameOne, text=' ', justify="left",width=19,background=ca.colorinstitucional)
        #col_vac.grid(row=8, column=0)
        num_lab = Label(self.frameOne, text='Numero',width=21,background=ca.colorinstitucional,fg="white")
        num_lab.grid(row=8, column=0)
        name_lab = Label(self.frameOne, text='Nombre', width=50,background=ca.colorinstitucional,fg="white")
        name_lab.grid(row=8, column=1)
        mark_lab = Label(self.frameOne, text='Nota', width=30,background=ca.colorinstitucional,fg="white")
        mark_lab.grid(row=8, column=2)
        mark_lab_acc = Label(self.frameOne, text='Nota acumulada', width=21,background=ca.colorinstitucional,fg="white")
        mark_lab_acc.grid(row=8, column=3)
        mark_lab_acc = Label(self.frameOne, text='Convocatoria', width=21,background=ca.colorinstitucional,fg="white")
        mark_lab_acc.grid(row=8, column=4)
        mark_lab_acc = Label(self.frameOne, text='Revisado', width=7,background=ca.colorinstitucional,fg="white")
        mark_lab_acc.grid(row=8, column=5)

        for index, course in enumerate(courses_list):
            if selection == course:
                yc_select = yellow_courses[index]
                ycn_select = yellow_curriculo_number[index]
        list_st = wfy.students(yc_select, ycn_select, ycl_select)
        self.num_piezas = len(list_st)

        self.scrollb.grid(row=1, column=1,sticky='nsew')  # grid scrollbar in master, because user had defined the numer of pieces


        self.n = 1
        while self.n <= int(self.num_piezas):
            self.num_st = Label(self.listFrame, text = list_st[self.n-1]['numero'],
                                    width=22,background=ca.colorinstitucional,fg="white")
            self.num_st.grid(row=self.n, column=0)
            self.nom_st = Label(self.listFrame, text = list_st[self.n-1]['nombre'],width=50)
            self.nom_st.grid(row=self.n, column=1)#, padx=(10,0))

            self.entrymark = Entry(self.listFrame,width=36,justify="center")
            self.entrymark.grid(row=self.n, column=2)#, padx=(0,10))
            self.entrymark.insert(0, "")

            self.entryacum = Entry(self.listFrame,width=25,justify="center")
            self.entryacum.grid(row=self.n, column=3)
            self.entryacum.insert(0, list_st[self.n-1]['acumulado'])

            self.entrycall = Entry(self.listFrame,width=36,justify="center")
            self.entrycall.grid(row=self.n, column=4)#, padx=(0,10))
            self.entrycall.insert(0, list_st[self.n-1]['convocatoria'])

            self.var1 = IntVar()
            self.entrynumlotes = Checkbutton(self.listFrame, variable=self.var1)
            self.entrynumlotes.grid(row=self.n, column=5, padx=(20,5))

            self.n += 1

        self.anadirpiezas = Button(self.frameThree, text="Cargar notas", command=self.addpieza, width=10)
        self.anadirpiezas.grid(row=0, column=2, pady=(10,10))


    def addpieza(self):
        print('hrllo')


if __name__ == "__main__":
    root = Tk()
    aplicacion = Planificador(root)
    root.mainloop()