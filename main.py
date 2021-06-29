#libraries and modules
from tkinter import *
import os

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
def main(): 
    def liste_menu ():
        menu.destroy()
        os.system("python ./pages/liste.py")

    def ajouter_menu ():
        menu.destroy()
        os.system("python ./pages/ajouter.py")

    def modifer_menu ():
        menu.destroy()
        os.system("python ./pages/modifier.py")

    def supprimer_menu ():
        menu.destroy()
        os.system("python ./pages/supprimer.py")

    def back_to_menu ():
        menu.destroy()
        os.system("python ../main.py")

    def quitter ():
        menu.destroy()
        os.system("exit")



    #initialisers
    menu = Tk(className= "Gestion des pays de la CEDEAO")
    menu.geometry("500x500")
    menu.configure(background=main_bg)

    #widgets
    mainText = Label( menu,text="Menu Principal",
                            bg=main_bg,
                            fg= header_fg,
                            width="90",
                            font=header_font,
                            pady = "10",
                            padx="10"
                            )
    mainText.pack(pady=20)

    afficher_btn = Button(menu, text="Liste des pays",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = liste_menu)

    afficher_btn.pack(pady=10)

    ajouter_btn = Button(menu, text="Ajouter un pays",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = ajouter_menu)

    ajouter_btn.pack(pady=10)

    supprimer_btn = Button(menu, text="Supprimer",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = supprimer_menu)

    supprimer_btn.pack(pady=10)

    modifier_btn = Button(menu, text="Modifier",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = modifer_menu)

    modifier_btn.pack(pady=10)

    quitter_btn = Button(menu, text="Quitter",
                                width = "30",
                                pady="10",
                                activebackground="black",
                                activeforeground = "white",
                                background = widget_bg,
                                font = main_font,
                                fg = main_fg,
                                command = quitter)

    quitter_btn.pack(pady=10)
    #mainloop
    menu.mainloop()



#EXECUTION
if __name__ == "__main__":
    main()
