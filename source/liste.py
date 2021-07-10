#libraries and modules
from tkinter import *
from tkinter import ttk

import os
import json
import tkinter as tk

from config import *

def afficher():

    def insert_data(data):
        for i in data:
            trv.insert("","end",values=(
                                        i,
                                        data[i]['nom'],
                                        data[i]['capital'],
                                        data[i]['population'],
                                        data[i]['langue'],
                                        data[i]['superficie'],
                                        data[i]['independance'],
                                        data[i]['president'],
                                        data[i]['pib']
                                        ))
    def ajouter_menu ():
        menu.destroy()
        os.system("python ./ajouter.py")

    def modifier_menu ():
        menu.destroy()
        os.system("python ./modifier.py")

    def supprimer_menu ():
        menu.destroy()
        os.system("python ./supprimer.py")

    def back_to_menu ():
        menu.destroy()
        os.system("python ./main.py")


    #initialisers
    menu = Tk(className= "Gestion des pays de la CEDEAO - Liste des pays")
    menu.geometry("1500x600")
    menu.configure(background=main_bg)

    #WRAPPER
    list_wrapper = LabelFrame(menu, text="Liste des Pays", height=300)
    button_wrapper = LabelFrame(menu, text="Utilitaire")

    #WIDGETS
    trv = ttk.Treeview(list_wrapper, columns=(1,2,3,4,5,6,7,8,9), show='headings', height='20')
    trv.pack()

    trv.heading(1,text="Code")
    trv.heading(2,text="Nom")
    trv.heading(3,text="Capital")
    trv.heading(4,text="Population")
    trv.heading(5,text="Langue")
    trv.heading(6,text="Superficie")
    trv.heading(7,text="Date d'Independance")
    trv.heading(8,text="President")
    trv.heading(9,text="PIB")


    retour_btn = Button(button_wrapper, text="retour",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = back_to_menu)

    ajouter_btn = Button(button_wrapper, text="Ajouter",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = ajouter_menu)

    supprimer_btn = Button(button_wrapper, text="Supprimer",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = supprimer_menu)


    modifier_btn = Button(button_wrapper, text="Modifier",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = modifier_menu)



    retour_btn.pack(side=tk.LEFT,pady=10)
    ajouter_btn.pack(side=tk.RIGHT,pady=10,padx=5)
    supprimer_btn.pack(side=tk.RIGHT,pady=10,padx=5)
    modifier_btn.pack(side=tk.RIGHT,pady=10,padx=5)


    #init Wrapper
    list_wrapper.pack(fill="both", expand="no", padx=20,pady=20)
    button_wrapper.pack(fill="both", expand="no", padx=20,pady=20)


    #grid System

    #conditions

    #Data init
    data = json.load(open("./config/assets/data.json"))
    insert_data(data)
    #mainloop
    menu.mainloop()

afficher()
