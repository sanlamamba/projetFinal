#libraries and modules
from tkinter import *  
from tkinter import ttk

import os
import json
import tkinter as tk

#DATA LOADING 
data = json.load(open("./config/assets/data.json"))


#functions
main_font = ('Arial', 12)
header_font = ('Arial Bold', 20)
secondary_font = ('Arial Narrow', 11)


#COLORS
header_fg = "#202020"
main_bg = "#efefff";
main_fg = "#fafafa"
widget_bg = "#303030"
#FUNTIONS

def insert_data(data):
    trv.delete(*trv.get_children())
    for i in data:
        trv.insert("","end",values=(
                                    i,
                                    data[i]['nom'],
                                    data[i]['capital']
                                    ))

def remove_country():
    global data
    print(data)
    try:
        int(code_txt.get())
    except:
        info_label['text']="Erreur : Veuillez remplir les champs correctement"
        return "Erreur : Veuillez remplir les champs correctement"

    code = int(code_txt.get())
    if str(code) not in data:
        info_label['text']="Erreur : L'element existe pas"
        return "Error"
    
    data.pop(str(code))
    out_file = open("./config/assets/data.json",'w');
    json.dump(data,out_file,indent=5)
    out_file.close()
    data = json.load(open("./config/assets/data.json"))
    insert_data(data)
    info_label['text']="L'element "+str(code)+" a ete retirer"
    code_txt.set("")
    return "Success"


def liste_menu ():
    menu.destroy()
    os.system("python ./pages/liste.py")

def ajouter_menu ():
    menu.destroy()
    os.system("python ./pages/ajouter.py")

def modifier_menu ():
    menu.destroy()
    os.system("python ./pages/modifier.py")

def supprimer_menu ():
    menu.destroy()
    os.system("python ./pages/supprimer.py")

def back_to_menu ():
    menu.destroy()
    os.system("python ./main.py")

def quitter ():
    menu.destroy()
    os.system("exit")



#initialisers
menu = Tk(className= "Gestion des pays de la CEDEAO - Liste des pays")
menu.geometry("1100x650")
menu.configure(background=main_bg)

#WRAPPER
        
entry_wrapper = LabelFrame(menu, text="Ajouter un pays")
button_wrapper = LabelFrame(menu, text="Utilitaire")
info_wrapper = LabelFrame(menu, text="Informations")

#WIDGETS
trv = ttk.Treeview(entry_wrapper, columns=(1,2,3), show='headings', height='10')
trv.grid(row=0,column=0,columnspan=2)

trv.heading(1,text="Code")
trv.heading(2,text="Nom")
trv.heading(3,text="Capital")

confirmation_wrapper = LabelFrame(entry_wrapper, text="Supprimer un pays", height=300)
confirmation_wrapper.grid(row=1,column=0,columnspan=2,padx=5,pady=5)
code_txt = StringVar()
code_label = Label(confirmation_wrapper, text="Code du pays", padx=5,font=main_font)
code_entry = Entry(confirmation_wrapper,textvariable=code_txt,width=40)
code_label.grid(row=0,column=0,pady=10,padx=10)
code_entry.grid(row=0,column=1,pady=10,padx=10,ipadx=20,ipady=5)

refresh_btn=Button(entry_wrapper,text="Rafraichir",width=20,pady=5,padx=5,activebackground="black",activeforeground="white",background=widget_bg,font=main_font,fg=main_fg)
refresh_btn.grid(row=3,column=1,padx=5,pady=5)

valider_btn=Button(entry_wrapper,text="valider",width=20,pady=5,padx=5,activebackground="black",activeforeground="white",background=widget_bg,font=main_font,fg=main_fg, command=remove_country)
valider_btn.grid(row=3,column=2,columnspan=2,padx=5,pady=5)


retour_btn = Button(button_wrapper, text="retour",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = widget_bg,
                            font = main_font,
                            fg = main_fg,
                            command = back_to_menu)


liste_btn = Button(button_wrapper, text="Liste",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = widget_bg,
                            font = main_font,
                            fg = main_fg,
                            command = liste_menu)



retour_btn.pack(side=tk.LEFT,pady=10)
liste_btn.pack(side=tk.RIGHT,pady=10,padx=5)


info_label = Label(info_wrapper, text="Remplir les informations pour commencer", padx=5,font=header_font)
info_label.pack()

#init Wrapper
entry_wrapper.pack(fill="both", expand="no", padx=20,pady=20)
button_wrapper.pack(fill="both", expand="no", padx=20,pady=20)
info_wrapper.pack(fill="both", expand="no", padx=20,pady=20)


#grid System

#conditions

#Data init
insert_data(data)
#mainloop
menu.mainloop()

