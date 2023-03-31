from tkinter import *
from tkinter import ttk
from Settings import config_paths as cp
from Displays.tasks_superuser import Planificador
import json
from Settings import media

paths = cp.paths()
ca = media.sttingsmedia()
#app = tasks_superuser.Planificador()

def validation():
    global credentials_window,entry_user, entry_psswd

    credentials_window = Tk()
    credentials_window.title("Introducir datos para ejecutar privilegios")
    credentials_window.geometry('400x125')  # 415+4, 497+3*18
    credentials_window.configure(background=ca.colorinstitucional)

    label_user = ttk.Label(credentials_window, text="Usuario (e-mail):")
    label_user.grid(row=0, column=0, sticky="w")
    user = StringVar()
    entry_user = ttk.Entry(credentials_window, textvariable=user, width=400)
    entry_user.grid(row=1, column=0, sticky="w")
    label_psswd = ttk.Label(credentials_window, text="Contraseña:")
    label_psswd.grid(row=2, column=0, sticky="w")
    psswd = StringVar()
    entry_psswd = ttk.Entry(credentials_window, textvariable=psswd, width=400)
    entry_psswd.grid(row=3, column=0, sticky="w")

    button_apply = ttk.Button(credentials_window, text="Entrar", command=enter)
    button_apply.grid(row=4, column=0, sticky="w")

def enter():
    user_introduced = entry_user.get()
    psswd_introduced = entry_psswd.get()

    with open(paths.privileges_path, 'r') as users_list:  # meter en config file file_users =
        data_users = json.load((users_list))
    flag = 0

    for user in data_users:
        if (data_users['name'] == user_introduced and data_users['psswd'] == psswd_introduced):
            flag = 2
            credentials_window.destroy()
            break
        elif (data_users['name'] == user_introduced):
            flag = 1
            break
    if (flag == 0):
        permissions = ['Usuario no encontrado']
        reply = ttk.Label(credentials_window, text=permissions, width=400)
        reply.grid(row=5, column=0)
    elif (flag == 1):
        permissions = ['Contraseña Incorrecta']
        reply = ttk.Label(credentials_window, text=permissions, width=400)
        reply.grid(row=5, column=0)
    elif (flag == 2):
        permissions = data_users['permissions']
        for index, rol in enumerate (permissions):
            if rol=="all":
                root = Tk()
                planificador = Planificador(root)
                root.mainloop()
                #app.master()
                break

    users_list.close()