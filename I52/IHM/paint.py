import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.filedialog

Longueur = 500
Largeur = 500

class fenetre(tk.Tk):
    
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.menu_bar()

        self.title("Test")

    def menu_bar(self):
        Nmenu= tk.Menu(self)
        menu_Fichier= tk.Menu(Nmenu, tearoff= 0)
        menu_Fichier.add_command(label= "Nouveau", command= self.Nouveau)
        menu_Fichier.add_command(label= "Ouvrir", command= self.Ouvrir)
        menu_Fichier.add_command(label= "Sauver", state= "disabled", command= self.Sauver)
        menu_Fichier.add_separator()
        menu_Fichier.add_command(label= "Quitter", command= self.Quitter)
        Nmenu.add_cascade(label= "Fichier", menu= menu_Fichier)

        menu_Aide = tk.Menu(Nmenu, tearoff=0)
        menu_Aide.add_command(label="About")
        Nmenu.add_cascade(label="Help", menu= menu_Aide)

        self.config(menu= Nmenu)

    def Nouveau(self):
        '''
        Fonction qui clean le canvas
        '''
        can.delete('all')

    def Ouvrir(self):
        '''
        Fonction qui clean le canvas et ouvre le fichier choisi
        '''
        filename= tkinter.filedialog.askopenfilename(title="Ouvrir votre document", filetypes=[('txt files','.txt'),('all files','.*')])
        can.delete("all")
        titre.config(text= filename)

    def Sauver(self):
        '''
        Fonction qui permet de sauvegarde le dessin
        '''
        f= tkinter.filedialog.asksaveasfile(title= "Enregistrer un fichier sous")

    def Quitter(self):
        '''
        Fonction pour quitter l'application
        '''
        if messagebox.askokcancel("Quitter", "Voulez vous quitter?"):
            root.quit()

def tracer(event, canevas):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    id = canevas.create_line(X, Y, event.x+1, event.y+1, fill='black', width= 2)
    canevas.bind('<Control-Button1-Motion>', lambda event: deplacement(event, id, canevas))

def deplacement(event, id, canevas):
    coordonné = canevas.coords(id)
    coordonné.append(event.x+1)
    coordonné.append(event.y+1)
    canevas.coords(id, tk._flatten(coordonné))

def change_rouge(event):
    """ met la couleur d'une ligne en rouge au passage de la souris """
    ligne = can.find_withtag("current")[0]
    can.itemconfig(ligne, fill= "red")

def change_noir(event):
    """ let la couleur d'une ligne en noir lorsque la souris s'enlève"""
    ligne = can.find_withtag("current")[0]
    can.itemconfig(ligne, fill= "black", width= 2)

root= tk.Tk()
root.title("Fenêtre Mère") # Nom de la fenetre mère

tns= fenetre()
tns.title("Paint")

frame = tk.Frame(tns)  # creation frame (carré blanc dans la fenetre)
frame.pack()

can = tk.Canvas(frame, bg= "white" ,width= Longueur, height= Largeur)
can.bind('<Control-1>', lambda event: tracer(event, can))
can.pack(side= "left", expand= True, fill= "both")

can.tag_bind("current", "<Enter>", change_rouge)
can.tag_bind("current", "<Leave>", change_noir)

titre = tk.Label(tns, bg= "LightBlue") # Création de label dans la fenetre fille
titre.pack(side= "bottom", fill= "x")

root.mainloop()

       
