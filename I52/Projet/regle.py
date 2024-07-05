import joueur

class Regles():

	def __init__(self):
		regle.__init__(self)
		self.type()

	def type(self):
		pass


	def action(self):
		pass
        
        
	def duel(self,joueur, nb): #il faudra déterminer comment savoir dans qu'elle règle nous sommes, j'applique pour le moment la règle avec la parade
	#La partie basique étant très simple à coder.
		'''
		Fonction pour le duel, return 1 servira pour signifier que l'attaque est réussi, 0 si elle est parée.
		'''
 
		if(joueur): #Joueur 1
			#partie attaque
			if(joueur.joueur1.main.count(nb)==1): #si le joueur n'a qu'une carte, c'est facile
				joueur.deck.defause+=[nb]
				attaque = (nb,1)
				joueur.joueur1.main.remove(nb) #fonction supprimant le premier nb croisé.
			else:
				val = int(input("Vous avez ",joueur.joueur1.main.count(nb)," cartes ", nb,".\n Combien voulez vous en jouer : ")) #il faudra remplacer ça par un clic sur les cartes que l'on veut sélectionner.
				attaque  = (nb, val)
				while(val !=0): #Je pense pas qu'on ai besoin de toucher à ça
					joueur.joueur1.main.remove(nb)
					joueur.deck.defause+=[nb]
					val-=1
    				
			#partie parade
			print(joueur.joueur2.main.count(nb))
			if((joueur.joueur2.main.count(nb)==0) or (joueur.joueur2.main.count(nb)<attaque[1])): #si le joueur 2 n'a pas assez de carte nb pour paré, l'attaque est valide
				return 1
				
			val = attaque[1] # si la parade est réussi, on défausse les cartes de parade de J2
			while(val !=0): 
	    			joueur.joueur2.main.remove(nb)
	    			joueur.deck.defause+=[nb]
	    			val-=1
			return 0	

		else:
			#partie attaque
			if(joueur.joueur2.main.count(nb)==1): #si le joueur n'a qu'une carte, c'est facile
				joueur.deck.defause+=[nb]
				attaque = (nb,1)
				joueur.joueur2.main.remove(nb) #fonction supprimant le premier nb croisé.
			else:
				val = int(input("Vous avez ",joueur.joueur2.main.count(nb)," cartes ", nb,".\n Combien voulez vous en jouer : ")) #il faudra remplacer ça par un clic sur les cartes que l'on veut sélectionner.
				attaque  = (nb, val)
				while(val !=0): #Je pense pas qu'on ai besoin de toucher à ça
					joueur.joueur2.main.remove(nb)
					joueur.deck.defause+=[nb]
					val-=1
    				
			#partie parade
			print(joueur.joueur1.main.count(nb))
			if((joueur.joueur1.main.count(nb)==0) or (joueur.joueur1.main.count(nb)<attaque[1])): #si le joueur 2 n'a pas assez de carte nb pour paré, l'attaque est valide
				return 1
				
			val = attaque[1] # si la parade est réussi, on défausse les cartes de parade de J2
			while(val !=0): 
	    			joueur.joueur1.main.remove(nb)
	    			joueur.deck.defause+=[nb]
	    			val-=1
			return 0
			
