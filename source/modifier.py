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
def rechercher_pays():
    global data
    if(code_txt.get() == ""):
        info_label['text']="Erreur : Veuillez remplir les champs correctement"
        return 0

  
    code = int(code_txt.get())
    if str(code) in data:
        code_entry.configure(state="disabled")
        recherche_btn.configure(state="disabled")
        print(data[str(code)]["nom"])

        

        name_entry.configure(state="normal")
        capital_entry.configure(state="normal")
        population_entry.configure(state="normal")
        langue_entry.configure(state="normal")
        superficie_entry.configure(state="normal")
        mois_entry.configure(state="normal")
        jour_entry.configure(state="normal")
        annee_entry.configure(state="normal")
        president_entry.configure(state="normal")
        pib_entry.configure(state="normal")
        refresh_btn.configure(state="normal")
        valider_btn.configure(state="normal")

        name_entry.delete(0,END)
        name_entry.insert(END,str(data[str(code)]["nom"]))
        capital_entry.delete(0,END)
        capital_entry.insert(END,str(data[str(code)]["capital"]))
        population_entry.delete(0,END)
        population_entry.insert(END,str(data[str(code)]["population"]))
        langue_entry.delete(0,END)
        langue_entry.insert(END,str(data[str(code)]["langue"]))
        superficie_entry.delete(0,END)
        superficie_entry.insert(END,str(data[str(code)]["superficie"]))
        president_entry.delete(0,END)
        president_entry.insert(END,str(data[str(code)]["president"]))
        pib_entry.delete(0,END)
        pib_entry.insert(END,str(data[str(code)]["pib"]))

        date = str(data[str(code)]["independance"]).split(sep="-")
        jour_entry.delete(0,END)
        jour_entry.insert(END,date[0])
        mois_entry.delete(0,END)
        mois_entry.insert(END,date[1])
        annee_entry.delete(0,END)
        annee_entry.insert(END,date[2])

        info_label['text']="Modifier les informations, puis  appuyer Valider"

    else:
        info_label['text']="Erreur : Cet code n'existe pas"
        return 0

def modifier_country():
    global data
    # print(data)
    try:
        int(code_txt.get())
        int(population_txt.get())
        int(superficie_txt.get())
        int(annee_txt.get())
        int(jour_txt.get())
        int(mois_txt.get())
        int(pib_txt.get())
    except:
        info_label['text']="Erreur : Veuillez remplir les champs correctement"
        return "Erreur : Veuillez remplir les champs correctement"

    code = int(code_txt.get())
    print(code)
    if str(code) not in data:
        info_label['text']="Erreur : Code n'existe pas"
        return "Erreur 807"
    else:

        nom = name_txt.get()
        capital = capital_txt.get()
        population = int(population_txt.get())
        langue = langue_txt.get()
        superficie = int(superficie_txt.get())
        
        annee = int(annee_txt.get())
        jour = int(jour_txt.get())
        mois = int(mois_txt.get())
        if((annee not in range(1800,2021)) or(jour not in range(0,31)) or(mois not in range(1,13))):
            info_label['text']="Erreur la date doit etre sous la forme AAAA -- JJ -- MM"
            return "Erreur la date"
        president= president_txt.get()
        pib = int(pib_txt.get())
        
        if((nom == "") or (capital == "") or (langue == "") or (president == "")):
            info_label['text']="Erreur : Veuillez remplir les champs correctement"
            return "Veuillez remplir les champs"

        data[str(code)] = {
            "nom":nom,
            "capital":capital,
            "population":population,
            "langue":langue,
            "superficie":superficie,
            "independance":str(jour)+"-"+str(mois)+"-"+str(annee),
            "president":president,
            "pib":pib
        }
        out_file = open("./config/assets/data.json",'w');
        json.dump(data,out_file,indent=5)
        out_file.close()
        info_label['text']="Modification de " +str(code)+" reussie"
        data=json.load(open("./config/assets/data.json"))
        return "success"


def liste_menu ():
    menu.destroy()
    os.system("python ./liste.py")

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

def quitter ():
    menu.destroy()
    os.system("exit")



#initialisers
menu = Tk(className= "Gestion des pays de la CEDEAO - Liste des pays")
menu.geometry("1100x800")
menu.configure(background=main_bg)

#WRAPPER
        
entry_wrapper = LabelFrame(menu, text="Ajouter un pays")
button_wrapper = LabelFrame(menu, text="Utilitaire")
info_wrapper = LabelFrame(menu, text="Informations")

#WIDGETS

name_txt = StringVar()
name_label = Label(entry_wrapper, text="Nom du pays", padx=5,font=main_font)
name_entry = Entry(entry_wrapper,textvariable=name_txt,width=50)
name_label.grid(row=1,column=0,pady=10,padx=10)
name_entry.grid(row=1,column=1,pady=10,padx=10,ipadx=20,ipady=5)

capital_txt = StringVar()
capital_label = Label(entry_wrapper, text="Capital du pays", padx=5,font=main_font)
capital_entry = Entry(entry_wrapper,textvariable=capital_txt,width=50)
capital_label.grid(row=1,column=2,pady=10,padx=10)
capital_entry.grid(row=1,column=3,pady=10,padx=10,ipadx=20,ipady=5)

population_txt = StringVar()
population_label = Label(entry_wrapper, text="Population du pays", padx=5,font=main_font)
population_entry = Entry(entry_wrapper,textvariable=population_txt,width=50)
population_label.grid(row=2,column=0,pady=10,padx=10)
population_entry.grid(row=2,column=1,pady=10,padx=10,ipadx=20,ipady=5)

langue_txt = StringVar()
langue_label = Label(entry_wrapper, text="langue du pays", padx=5,font=main_font)
langue_entry = Entry(entry_wrapper,textvariable=langue_txt,width=50)
langue_label.grid(row=2,column=2,pady=10,padx=10)
langue_entry.grid(row=2,column=3,pady=10,padx=10,ipadx=20,ipady=5)

superficie_txt = StringVar()
superficie_label = Label(entry_wrapper, text="superficie du pays", padx=5,font=main_font)
superficie_entry = Entry(entry_wrapper,textvariable=superficie_txt,width=50)
superficie_label.grid(row=3,column=0,pady=10,padx=10)
superficie_entry.grid(row=3,column=1,pady=10,padx=10,ipadx=20,ipady=5)



president_txt = StringVar()
president_label = Label(entry_wrapper, text="president", padx=5,font=main_font)
president_entry = Entry(entry_wrapper,textvariable=president_txt,width=50)
president_label.grid(row=4,column=0,pady=10,padx=10)
president_entry.grid(row=4,column=1,pady=10,padx=10,ipadx=20,ipady=5)

pib_txt = StringVar()
pib_label = Label(entry_wrapper, text="pib", padx=5,font=main_font)
pib_entry = Entry(entry_wrapper,textvariable=pib_txt,width=50)
pib_label.grid(row=4,column=2,pady=10,padx=10)
pib_entry.grid(row=4,column=3,pady=10,padx=10,ipadx=20,ipady=5)

code_txt = StringVar()
code_label = Label(entry_wrapper, text="Code du pays", padx=5,font=main_font)
code_entry = Entry(entry_wrapper,textvariable=code_txt,width=40)
code_label.grid(row=0,column=0,pady=10,padx=10)
code_entry.grid(row=0,column=1,pady=10,padx=10,ipadx=20,ipady=5)
recherche_btn = Button(entry_wrapper, text="Rechercher",
                            # width = "30",
                            # pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = widget_bg,
                            font = main_font,
                            fg = main_fg,
                            command = rechercher_pays)
recherche_btn.grid(row=0,column=2,pady=10,padx=10,ipadx=20,ipady=5)

date_wrapper = LabelFrame(entry_wrapper, text="Date d'independance", height=300)
date_wrapper.grid(row=5,column=0,columnspan=4,padx=5,pady=5)

annee_txt = StringVar()
annee_label = Label(date_wrapper, text="annee", padx=5,font=main_font)
annee_entry = Entry(date_wrapper,textvariable=annee_txt,width=15)
annee_label.grid(row=0,column=0,pady=10,padx=10)
annee_entry.grid(row=0,column=1,pady=10,padx=10,ipadx=20,ipady=5)

jour_txt = StringVar()
jour_label = Label(date_wrapper, text="jour", padx=5,font=main_font)
jour_entry = Entry(date_wrapper,textvariable=jour_txt,width=15)
jour_label.grid(row=0,column=2,pady=10,padx=10)
jour_entry.grid(row=0,column=3,pady=10,padx=10,ipadx=20,ipady=5)

mois_txt = StringVar()
mois_label = Label(date_wrapper, text="mois", padx=5,font=main_font)
mois_entry = Entry(date_wrapper,textvariable=mois_txt,width=15)
mois_label.grid(row=0,column=4,pady=10,padx=10)
mois_entry.grid(row=0,column=5,pady=10,padx=10,ipadx=20,ipady=5)

name_entry.configure(state="disabled")
capital_entry.configure(state="disabled")
population_entry.configure(state="disabled")
langue_entry.configure(state="disabled")
superficie_entry.configure(state="disabled")
mois_entry.configure(state="disabled")
jour_entry.configure(state="disabled")
annee_entry.configure(state="disabled")
president_entry.configure(state="disabled")
pib_entry.configure(state="disabled")
refresh_btn=Button(entry_wrapper,text="Rafraichir",width=20,pady=5,padx=5,activebackground="black",activeforeground="white",background=widget_bg,font=main_font,fg=main_fg)
refresh_btn.grid(row=6,column=0,columnspan=2,padx=5,pady=5)

valider_btn=Button(entry_wrapper,text="valider",width=20,pady=5,padx=5,activebackground="black",activeforeground="white",background=widget_bg,font=main_font,fg=main_fg, command=modifier_country)
valider_btn.grid(row=6,column=3,columnspan=2,padx=5,pady=5)
valider_btn.configure(state="disabled")
refresh_btn.configure(state="disabled")


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


info_label = Label(info_wrapper, text="Rechercher le pays a modifier pour commencer ", padx=5,font=header_font)
info_label.pack()

#init Wrapper
entry_wrapper.pack(fill="both", expand="no", padx=20,pady=20)
button_wrapper.pack(fill="both", expand="no", padx=20,pady=20)
info_wrapper.pack(fill="both", expand="no", padx=20,pady=20)

menu.mainloop()

