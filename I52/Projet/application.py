import tkinter as tk
from tkinter.messagebox import *
from PIL import Image, ImageTk
import webbrowser
import jeu
import joueur
import regle

Hauteur = 700
Largeur = 1000

class fenetre(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.menu_bar()

    def menu_bar(self):
        Nmenu = tk.Menu(self)
        helpmenu = tk.Menu(Nmenu, tearoff= 0)
        helpmenu.add_command(label= "A propos", command= bouton_apropos)
        Nmenu.add_cascade(label= "Aide", menu= helpmenu)


        self.config(menu= Nmenu)


def checkbutton_etat():
    '''
    Fonction qui Active ou Désactive les checkbuttons
    '''
    if checkbutton_var.get():
        b3['state'] = "disabled"
        b4['state'] = "disabled"
    elif checkbutton_var2.get():
        b2['state'] = "disabled"
        b4['state'] = "disabled"
    elif checkbutton_var3.get():
        b2['state'] = "disabled"
        b3['state'] = "disabled"
    else:
        b2['state'] = "normal"
        b3['state'] = "normal"
        b4['state'] = "normal"


def bouton_play():
    '''
    Fonction qui servira pour le bouton "Jouer"
    '''
    if checkbutton_var.get():
        result = tk.messagebox.askyesno("Confirmation", "Veux-tu lancer une partie avec les règles de base ?")
        if result:
            print("Lancement de la partie (base)")
            jeu.clean(can)
            jeu.plateau(can)                # Note: Ecrire une classe qui regroupe l'ensemble de ces fonctions
            jeu.pioche_defausse(can)
            jeu.affichage_main(can)
            joueur1= joueur.Joueur("j1")
            joueur2= joueur.Joueur("j2")
            #appli_base() lancera le jeu avec les règles de base
        else:
            print("Retour a l'accueil")
    elif checkbutton_var2.get():
        result = tk.messagebox.askyesno("Confirmation", "Veux-tu lancer une partie avec les règles classique ?")
        if result:
            print("Lancement de la partie (classique)")
            jeu.clean(can)
            jeu.plateau(can)                # Note: Ecrire une classe qui regroupe l'ensemble de ces fonctions
            jeu.pioche_defausse(can)
            jeu.affichage_main(can)
            joueur1= joueur.Joueur("j1")
            joueur2= joueur.Joueur("j2")
            # lancera le jeu avec les règles classique
        else:
            print("Retour a l'accueil")
    elif checkbutton_var3.get():
        result = tk.messagebox.askyesno("Confirmation", "Veux-tu lancer une partie avec les règles avancée ?")
        if result:
            print("Lancement de la partie (avancée)")
            jeu.clean(can)
            jeu.plateau(can)                # Note: Ecrire une classe qui regroupe l'ensemble de ces fonctions
            jeu.pioche_defausse(can)
            jeu.affichage_main(can)
            j1= joueur.Joueur("j1")
            j2= joueur.Joueur("j2")
            #appli_avancée() lancera le jeu avec les règles avancée
        else:
            print("Retour a l'accueil")
    pass

def bouton_apropos():
    webbrowser.open("https://nguyen.univ-tln.fr/share/IHM/engarde-regles.pdf")

def mouvement(event):
    '''
    Fonction qui déplace les marqueurs score
    '''
    id = can.gettags("current")[0]
    if id == "score_j1":
        can.move(id, 42, 0)
    elif id == "score_j2":
        can.move(id, -42, 0)

def taille_pioche(event):
    '''
    Affichage du nombres de cartes restantes dans la pioche
    '''
    id = can.gettags("current")[0]
    if id == "pioche":
        message= joueur.Deck.taille_pioche(joueur.deck)
        tk.messagebox.showinfo("Nombres de cartes restantes: ", message)

root = fenetre() # Fenetre mère
root.title("Fenêtre du jeu") # Nom de la fenetre mère

frame = tk.Frame(root) # Creation frame
frame.pack(side= "top")

can = tk.Canvas(frame, width= Largeur, height= Hauteur) # Fenetre taille Largeur*Hauteur fond blanc
can.pack()

can.create_text(500, 50, text= "En Garde!")

im = Image.open("en_garde.jpg") # Ouvre l'image en parametre
imp =  ImageTk.PhotoImage(im)
id = can.create_image(500, 300, image= imp) # Place l'image dans le canvas aux coordonnees

# Création des variables pour store les états des boutons
checkbutton_var = tk.IntVar()
checkbutton_var2 = tk.IntVar()
checkbutton_var3 = tk.IntVar()

# Initialise les valeurs des états des boutons
checkbutton_var.set(0)
checkbutton_var2.set(0)
checkbutton_var3.set(0)

b= tk.Button(can, text= "Jouer", command= bouton_play) # Création d'un bouton dans le canvas
can.create_window(500, 500, window= b) # Placage du centre du bouton aux coordonnées du canvas.

b2= tk.Checkbutton(can, text= "Règle de base",  variable= checkbutton_var, command= checkbutton_etat) # Création d'un check bouton "Règle de base" dans le canvas
can.create_window(500, 550, window= b2)

b3= tk.Checkbutton(can, text= "Règle classique", variable= checkbutton_var2, command= checkbutton_etat) # Création d'un check bouton "Règle classique" dans le canvas
can.create_window(500, 570, window= b3)

b4= tk.Checkbutton(can, text= "Règle avancée", variable= checkbutton_var3, command= checkbutton_etat) # Création d'un check bouton "Règle avancée" dans le canvas
can.create_window(500, 590, window= b4)


frame2 = tk.Frame(root)  # creation frame
frame2.pack(side= "bottom")

Button1=tk.Button(frame2, text="Quitter", command= root.quit)  # Bouton "OK" pour quitter l'application
Button1.pack(side= "left")

can.tag_bind("current", "<1>", taille_pioche)

root.mainloop()
