import numpy as np

class Vecteur3D:
    def __init__(self, origine, extremite):
        self.origine = origine
        self.extremite = extremite

    def __add__(self, vecteur):
        return Vecteur3D(self.origine, self.extremite + vecteur.extremite)
    
    def __sub__(self, vecteur):
        return Vecteur3D(self.origine, self.extremite - vecteur.extremite)
    
    def __mul__(self, scalaire):
        return Vecteur3D(self.origine, self.extremite * scalaire)
    
    def __truediv__(self, scalaire):
        return Vecteur3D(self.origine, self.extremite / scalaire)
    
    def produit_scalaire(self, vecteur):
        return np.dot(self.extremite, vecteur.extremite)
    
    def produit_vectoriel(self, vecteur):
        return Vecteur3D(self.origine, np.cross(self.extremite, vecteur.extremite))
    
    def norme(self):
        return np.linalg.norm(self.extremite)
    
    def normaliser(self):
        return Vecteur3D(self.origine, self.extremite / self.norme())
        