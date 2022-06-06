#!/usr/bin/python3

from struct import pack
from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import show
from Perudo import *

#Création de la fenêtre
window = Tk()
window.title("Calculateur Perudo")
window.geometry("1280x1280")
window.config(background='#dbca3a')

titre = Label(window, text="Bienvenue sur le calculateur de proba du Perudo", font=("Arial", 30), bg="#dbca3a", fg="#3adb97")
titre.pack(expand=YES)

des_list = [i for i in range(1,31)]
value_dice_list = [i for i in range(1,7)]
des_perso_list = [i for i in range(1,6)]
Bool = [0, 1]
total_dice = IntVar()
value_dice = IntVar()
bet = IntVar()
dice = IntVar()
nb_value = IntVar()
palifico = IntVar()

#Dés Totaux
total_dice_display = Label(window, text="Nombre Total de Dés :", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
total_dice_display.pack(expand=YES)
total_dice_entry = OptionMenu(window, total_dice, *des_list)
total_dice_entry.pack(expand=YES)

#Valeur de notre dé
value_dice_display = Label(window, text="Votre Valeur de Dé sur laquelle vous pariez:", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
value_dice_display.pack(expand=YES)
value_dice_entry = OptionMenu(window, value_dice, *value_dice_list)
value_dice_entry.pack(expand=YES)

#Notre Pari 
bet_display = Label(window, text="Vous pariez qu'il y'a au moins ?", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
bet_display.pack(expand=YES)
bet_entry = OptionMenu(window, bet, *des_list)
bet_entry.pack(expand=YES)

#Nos dés
dice_display = Label(window, text="Combien de dés possédez vous au total ?", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
dice_display.pack(expand=YES)
dice_entry = OptionMenu(window, dice, *des_perso_list)
dice_entry.pack(expand=YES)

#Nombre de dés que l'on a 
nb_value_display = Label(window, text=f"Combien de dés sur lequel vous pariez possèdez-vous ?", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
nb_value_display.pack(expand=YES)
nb_value_entry = OptionMenu(window, nb_value, *des_perso_list)
nb_value_entry.pack(expand=YES)

#Round Palifico ou non ?
palifico_display = Label(window, text="Round Palifico ?", font=('Helvetica', 15),bg="#dbca3a", fg="#a05252")
palifico_display.pack(expand=YES)
palifico_entry = OptionMenu(window, palifico, *Bool)
palifico_entry.pack(expand=YES)


def show():
    if nb_value.get() > dice.get() or nb_value.get() <0 :
        messagebox.showerror("Résultat",f"Votre nombre de {value_dice.get()} n'est pas bon")
    elif bet.get() > total_dice.get() :
        messagebox.showerror("Résultat",f"Votre pari n'est pas bon")
    else :
        proba = perudo_display(total_dice.get(), value_dice.get(), bet.get(), dice.get(), nb_value.get(), palifico.get())
        messagebox.showinfo("Résultat",f"La probabilité que ton pari soit bon est de {proba}")

myButton = Button(window, text="Calculer la Probabilité", command=show)
myButton.pack()
#Affichage fenetre
window.mainloop()