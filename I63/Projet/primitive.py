import numpy as np
from vecteurs import Vecteur3D

class Primitive:
    def __init__(self, position, couleur, materiau, max_profondeur = 1, ombre = True):
        self.position = position
        self.couleur = couleur
        self.materiau = materiau
        self.max_profondeur = max_profondeur
        self.ombre = ombre

    def intersection(self, origine, direction):
        raise NotImplementedError("intersection() must be implemented by subclass")

    def normale(self, point):
        raise NotImplementedError("normale() must be implemented by subclass")