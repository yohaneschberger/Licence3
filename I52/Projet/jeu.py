import tkinter as tk
from tkinter.messagebox import *
import joueur

# !# WARNING: En faire une classe

def clean(canvas):
    '''
    Fonction qui clean le canvas
    '''
    canvas.delete("all")

def plateau(canvas):
    '''
    Fonction qui crée le plateau de jeu
    '''
    i, j = 20, 300
    for case in range(23):
        canvas.create_rectangle(i, j, i+42, j+100, fill= "white")
        if case == 0:
            canvas.create_oval(i, j+105, i+42, j+130, fill= "black", tags= "score_j1")
            canvas.create_oval(i+5, j+10, i+37, j+45, fill= "red", tags= "j1")
        elif case == 22:
            canvas.create_oval(i, j+105, i+42, j+130, fill= "black", tags= "score_j2")
            canvas.create_oval(i+5, j+10, i+37, j+45, fill= "blue", tags= "j2")
        canvas.pack()
        i += 42

    i = 20
    for numleft in range(12):
        canvas.create_text(i+20, j+85, text= str(numleft))
        canvas.pack()
        i += 42

    i = 970
    for numright in range(11):
        canvas.create_text(i-5, j+85, text= str(numright))
        canvas.pack()
        i -= 42

def pioche_defausse(canvas):
    '''
    Fonction qui crée la pioche et la défausse
    '''
    i , j = 100, 50
    canvas.create_text(i, j, text= "Défausse :")
    canvas.create_text(i+800, j, text= "Pioche :")
    canvas.create_rectangle(i-50, j+30, i+50, j+180, fill= "black", tags= "defausse")
    canvas.create_rectangle(i+750, j+30, i+850, j+180, fill= "white", tags= "pioche")
    canvas.pack()

def affichage_main(canvas):
    '''
    Fonction qui affiche la main dans l'interface
    '''
    i, j = 250, 500 
    for case in range(5):
        canvas.create_rectangle(i, j, i+100, j+200, fill= "white", tags= "carte")
        canvas.create_text(i+50, j+100, text= joueur.joueur1.main[case])
        i += 100
    canvas.pack()

def historique(canvas):
    '''
    Fonction qui affichera l'action du joueur adverse
    '''
    pass
