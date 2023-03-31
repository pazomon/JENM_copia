from tkinter import *
from tkinter import ttk
from Settings import config_paths as cp
from Displays import accreditation as da
from Settings import media

paths = cp.paths()
ca = media.sttingsmedia()

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Jefatura de Estudios de la Escuela Naval Militar")
        self.raiz.geometry('419x551')#415+4, 497+3*18
        self.raiz.configure(background=ca.colorinstitucional)
        escudo = PhotoImage(file=paths.media_resources+'/escudo.png')
        escudo.configure()
        self.image_escudo = ttk.Label(self.raiz, image=escudo, anchor="center")
        self.image_escudo.grid( row=2, column=0)#, columnspan=2, rowspan=2)
        self.image_escudo = ttk.Label(self.raiz, image=escudo, anchor="center")
        self.image_escudo.grid( row=2, column=0)#, columnspan=2, rowspan=2)

        self.button_start = ttk.Button(self.raiz, text="Iniciar sesión", command=da.validation, width=13)
        self.button_start.grid(row=0, column=0)

        self.button_contact = ttk.Button(self.raiz, text="Contacto", command=self.contact, width=13)
        self.button_contact.grid(row=3, column=0)

        self.raiz.mainloop()

    def contact(self):
        print('h')

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
