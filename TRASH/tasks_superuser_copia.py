from tkinter import *
from tkinter import ttk
import tkinter
from Wanted_functions import yellow as wfy
import canvas

def tasks():
    global tasks_window
    tasks_window = tkinter.Tk()
    tasks_window.title("Tareas asignadas al rol Jefatura de Estudios")
    tasks_window.geometry('719x551')  # 415+4+200, 497+3*18
    tasks_window.configure(background='#173763')

    button_instud = ttk.Button(tasks_window, text="Introducir alumnos", width=20)
    button_instud.grid(row=0, column=0)
    
    button_insub = ttk.Button(tasks_window, text="Introducir asignaturas", width=20)
    button_insub.grid(row=1, column=0)
    
    button_inmarks = ttk.Button(tasks_window, text="Introducir notas", command=inmark, width=20)
    button_inmarks.grid(row=2, column=0)

def inmark():
    button_im_single = ttk.Button(tasks_window, text="Individual", width=20)
    button_im_single.grid(row=2, column=1)

    button_im_group = ttk.Button(tasks_window, text="Grupal", command=img, width=20)
    button_im_group.grid(row=3, column=1)

    button_im_load = ttk.Button(tasks_window, text="Carga de archivo", width=20)
    button_im_load.grid(row=4, column=1)

def img():
    global ycl_desplegable,yellow_courses, yellow_curriculo_number,courses_list

    yellow_courses, yellow_curriculo_number,courses_list = wfy.courses()
    yc_list = tkinter.StringVar()
    ycl_desplegable = ttk.Combobox(tasks_window, textvariable=yc_list, width=30)
    ycl_desplegable['values'] = courses_list
    ycl_desplegable.grid(row=3, column=2, sticky="e")
    button_yclsc = ttk.Button(tasks_window, text="Seleccionar curso", command=img_subjects, width=20)
    button_yclsc.grid(row=2, column=2)

def img_subjects():
    ycl_select = ycl_desplegable.get()
    for index, course in enumerate (courses_list):
        if ycl_select == course:
            yc_select = yellow_courses[index]
            ycn_select = yellow_curriculo_number[index]
    list_st = wfy.students(yc_select, ycn_select)

    mark_perc = IntVar
    mark_perc_acc = IntVar
    mark_perc_lab = ttk.Label(tasks_window, text='Avance evaluación')
    mark_perc_lab.grid(row=5, column=0)
    mark_perc_ent = ttk.Entry(tasks_window, textvariable=mark_perc)
    mark_perc_ent.grid(row=5, column=1)
    mark_perc_lab_acc = ttk.Label(tasks_window, text='Avance asignatura')
    mark_perc_lab_acc.grid(row=5, column=2)
    mark_perc_ent_acc = ttk.Entry(tasks_window, textvariable=mark_perc_acc)
    mark_perc_ent_acc.grid(row=5, column=3)

    num_lab = ttk.Label(tasks_window, text='Numero')
    num_lab.grid(row=6, column=0)
    name_lab = ttk.Label(tasks_window, text='Nombre')
    name_lab.grid(row=6, column=1)
    mark_lab = ttk.Label(tasks_window, text='Nota')
    mark_lab.grid(row=6, column=2)
    mark_lab_acc = ttk.Label(tasks_window, text='Nota acumulada')
    mark_lab_acc.grid(row=6, column=3)

    marco_contenedor = Frame(tasks_window, background='black')
    #marco_contenedor.col#geometry('719x451')
    marco_contenedor.grid(row=7)
    
    mark = IntVar
    mark_acc = IntVar
    #scroll = ttk.Scrollbar(tasks_window, orient=tkinter.VERTICAL)
    #scroll.grid(row=1, column=5, rowspan=2)

    for i in range(len(list_st)):
        num_lab_i = ttk.Label(marco_contenedor, text=list_st[i]['nombre'])
        num_lab_i.grid(row=7+i, column=0)
        name_lab_i = ttk.Label(marco_contenedor, text=list_st[i]['numero'])
        name_lab_i.grid(row=7+i, column=1)
        mark_ent_i = ttk.Entry(marco_contenedor, textvariable=mark)
        mark_ent_i.grid(row=7+i, column=2)
        mark_ent_acc_i = ttk.Entry(marco_contenedor, textvariable=mark_acc)
        mark_ent_acc_i.grid(row=7+i, column=3)

    #scroll = ttk.Scrollbar(tasks_window, orient='vertical',command=tasks_window.yview)
    #scroll.grid(row=0, column=5)
    #tasks_window['yscrollcommand']=scroll.set
    #scroll = tkinter.Scrollbar(tasks_window)
    #c = tkinter.Canvas(tasks_window,background='#173763',yscrollcommand=scroll.set)
    #scroll.config(command=c.yview())
    #scroll.grid(row=0, column=5)
    #scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    #marco = tkinter.Frame(c)
    #c.pack(side="left", fill="both",expand=True)
    #c.create_window(0,0,window=marco)
    #c.config(scrollregion=c.bbox("all"))
    #tasks_window.mainloop()
    #scroll.set()

def img_students():
    #leer json para poder escribir alumnos
    #with open(paths.yellow_path, "r") as json_file:
    #    summary_json = json.load(json_file)

    print('hello')
