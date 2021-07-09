import os

def liste_menu (container):
    container.destroy()
    os.system("python ./pages/liste.py")

def ajouter_menu (container):
    container.destroy()
    os.system("python ./pages/ajouter.py")

def modifier_menu (container):
    container.destroy(container)
    os.system("python ./pages/modifier.py")

def supprimer_menu (container):
    container.destroy()
    os.system("python ./pages/supprimer.py")

def back_to_menu (container):
    container.destroy(container)
    os.system("python ./main.py")

def quitter (container):
    container.destroy()
    os.system("exit")

