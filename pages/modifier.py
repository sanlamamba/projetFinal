#libraries and modules
from tkinter import *
import os

#functions
main_font = ('Arial Narrow', 11)
header_font = ('Arial Rounded Mt Bold', 24)
secondary_font = ('Arial Narrow', 11)


#COLORS
main_bg = "#ccccfa";
main_fg = "#202020"

#FUNTIONS
def gameStart ():
    menu.destroy()
    os.system("python loop.py")
def quitter ():
    menu.destroy()
    os.system("exit")



#initialisers
menu = Tk(className= "gestionnaire")
menu.geometry("720x640")
menu.configure(background=main_bg)

#widgets
mainText = Label( menu,text="Gestion des pays de la CEDEAO",
                        bg=main_bg,
                        fg= main_fg,
                        width="90",
                        font=header_font,
                        pady = "10",
                        padx="10"
                         )
mainText.pack()

afficher_btn = Button(menu, text="Liste des pays",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = "#aaaafa",
                            font = main_fg,
                            fg = main_fg,
                            command = gameStart)

afficher_btn.pack()

ajouter_btn = Button(menu, text="Ajouter un pays",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = "#faffaa",
                            font = main_fg,
                            fg = main_fg,
                            command = gameStart)

ajouter_btn.pack()

supprimer_btn = Button(menu, text="Supprimer",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = main_bg,
                            font = main_fg,
                            fg = main_fg,
                            command = gameStart)

supprimer_btn.pack()

modifier_btn = Button(menu, text="Modifier",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = main_bg,
                            font = main_fg,
                            fg = main_fg,
                            command = gameStart)

modifier_btn.pack()

quitter_btn = Button(menu, text="Quitter",
                            width = "30",
                            pady="10",
                            activebackground="black",
                            activeforeground = "white",
                            background = main_bg,
                            font = main_fg,
                            fg = main_fg,
                            command = quitter)

quitter_btn.pack()


#conditions

#mainloop
menu.mainloop()

