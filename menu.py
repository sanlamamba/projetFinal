from config import *
#initialisers
def menu():
     
     def liste_menu ():
          menu.destroy()
          os.system("python ./liste.py")

     def ajouter_menu ():
          menu.destroy()
          os.system("python ./ajouter.py")

     def modifier_menu ():
          menu.destroy()
          os.system("python ./modifier.py")
          
     def recherche_menu ():
          menu.destroy()
          os.system("python ./rechercher.py")

     def supprimer_menu ():
          menu.destroy()
          os.system("python ./supprimer.py")

     def quitter ():
          menu.destroy()
          os.system("exit")


     menu = Tk(className= "Gestion des pays de la CEDEAO")
     menu.geometry("500x600")
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
                                   command = modifier_menu)

     modifier_btn.pack(pady=10)

     recherche_btn = Button(menu, text="Rechercher",
                                   width = "30",
                                   pady="10",
                                   activebackground="black",
                                   activeforeground = "white",
                                   background = widget_bg,
                                   font = main_font,
                                   fg = main_fg,
                                   command = recherche_menu)

     recherche_btn.pack(pady=10)

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
     
     menu.mainloop()
menu()