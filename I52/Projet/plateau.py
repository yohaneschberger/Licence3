import joueur
import regle

class Plateau():
	def __init__(self):
		self.position_J1 = 0
		self.position_J2 = 23 #Les positions des joueurs changeront durant la partie, mais devront être réinitialiser avant chaque manche.
		self.bord1=0
		self.bord2=23 #les deux bords sont imuables.
		self.point_J1 = 0
		self.point_J2 = 0 #les points changeront, naturellement
	
	def __str__(self):
		return f"Position du joueur 1 : {self.position_J1}\nPosition du joueur 2 : {self.position_J2}"
		
	def deplacement(self, joueur, nb): #joueur est, pour le moment, une valeur binaire (1 pour j1, 0 pour j2)
		'''
		La fonction déplacement prend en compte toutes les possibilités (avanccé, recul, duel) et applique le choix du joueur. le return 0 signifie que le joueur 
		ne peut ou ne veut pas déplacer son pion. On s'en servira comme d'une annulation afin de lui faire rechoisir une carte plus en adaptée.
		'''
		if(joueur): #joueur 1
			if((self.position_J1-nb < bord1) and (self.position_J1 + nb >position_J2)): #on montre au joueur les mouvements qui ne sont pas faisable avec la carte sélectionnée
				print("valeur de carte non valide, déplacement avant et arrière impossible") #Si aucune action n'est possible, on annule directement pour changer de carte
				return 0
			elif(self.position_J1-nb < bord1):
				print("Recul impossible")
				if(self.position_J1 + nb == position_J2):
					reponse = int(input('Duel ? (0/1) : '))
					
					if(reponse):
						victoire_manche = regle.duel(joueur, nb) #fonction pour le duel, voir règle.py
						if(victoire_manche):
							self.point_J1+=1
							if(self.point_J1 == 5):
								print("Fin de partie. \n Victoire J1")
							return 1
						
				else:
					reponse = int(input('Avancer ? (0/1) : '))
					if(reponse):
						self.position_J1 += nb
						return 1
						
			elif(self.position_J1 + nb >position_J2):
				print("Avancé impossible")
				reponse = int(input('Reculer ? (0/1) : '))
				if(reponse):
					self.position_J1 -= nb
					return 1
						
			else: #ici, le recul, l'avancé et le duel sont tous possibles
				if(self.position_J1 + nb == position_J2):
					reponse = int(input('Duel ? (0/1) : '))
					
					if(reponse):
						victoire_manche = regle.duel(joueur, nb) 
						if(victoire_manche):
							self.point_J1+=1
							if(self.point_J1 == 5):
								print("Fin de partie. \n Victoire J1")
							return 1
						
				else:
					reponse = int(input('Avancer ? (0/1) : '))
					if(reponse):
						self.position_J1 += nb
						return 1
				
				reponse = int(input('Reculer ? (0/1) : '))
				if(reponse):
					self.position_J1 -= nb
					return 1
		
		else: #joueur 2
			if((self.position_J2+nb > bord2) and (self.position_J2 - nb <position_J1)):
				print("valeur de carte non valide, déplacement avant et arrière impossible")
				return 0
			elif(self.position_J2+nb > bord2):
				print("Recul impossible")
				if(self.position_J2 - nb == position_J1):
					reponse = int(input('Duel ? (0/1) : '))
					
					if(reponse):
						victoire_manche = regle.duel(joueur, nb) 
						if(victoire_manche):
							self.point_J2+=1
							if(self.point_J2 == 5):
								print("Fin de partie. \n Victoire J1")
							return 1
						
				else:
					reponse = int(input('Avancer ? (0/1) : '))
					if(reponse):
						self.position_J2 -= nb
						return 1
						
			elif(self.position_J2 - nb <position_J1):
				print("Avancé impossible")
				reponse = int(input('Reculer ? (0/1) : '))
				if(reponse):
					self.position_J2 += nb
					return 1
						
			else: #ici, le recul, l'avancé et le duel sont tous possibles
				if(self.position_J2 - nb == position_J1):
					reponse = int(input('Duel ? (0/1) : '))
					
					if(reponse):
						victoire_manche = regle.duel(joueur, nb) 
						if(victoire_manche):
							self.point_J2 += 1
							if(self.point_J2 == 5):
								print("Fin de partie. \n Victoire J1")
							return 1
						
				else:
					reponse = int(input('Avancer ? (0/1) : '))
					if(reponse):
						self.position_J2 -= nb
						return 1
				
				reponse = int(input('Reculer ? (0/1) : '))
				if(reponse):
					self.position_J2 += nb
					return 1
		return 0 #on arrive ici si le joueur n'est satisfait d'aucune possibilité proposée, donc on lui demandera de changer de carte.
			
