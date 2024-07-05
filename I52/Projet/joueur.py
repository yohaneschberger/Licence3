import random

class Joueur():

    def __init__(self, pion):
        self.pion= pion
        self.main= []

    def __str__(self):
        return f"main de {self.pion} : {self.main}"

    def piocher(self, deck):
        while(len(self.main)<5):
            self.main+= [int(f"{deck.cartes.pop()}")]

class Carte():
    '''
    Classe qui definit une carte
    '''
    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return f"{self.numero}"

class Deck():
    '''
    Classe qui initialise le deck de la manche
    '''

    def __init__(self):
        self.cartes= []
        for i in range(1,6) :
            self.cartes+= [Carte(i)]
        self.cartes*= 5
        self.defausse = []
      

    def melange(self):
        '''
        melange l'objet deck a chaque debut de manche
        '''
        random.shuffle(self.cartes)

    def distribution(self, j1, j2):
        '''
        distribue 5 cartes en debut de manche aux joueurs
        '''
        i=0
        while(i<5):
            j1.main+= [int(f"{self.cartes.pop()}")]
            j2.main+= [int(f"{self.cartes.pop()}")]
            i+=1
    
    def taille_pioche(self):
        return len(self.cartes)


deck = Deck()   #Creation d'un deck

Deck.melange(deck)  #Melange le deck

joueur1= Joueur("j1")
joueur2= Joueur("j2")

deck.distribution(joueur1,joueur2)

