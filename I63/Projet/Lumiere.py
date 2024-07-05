import numpy as np

class Lumiere:
    def __init__(self, position, couleur):
        self.position = position
        self.couleur = couleur

    def direction(self, point):
        return (self.position - point).normaliser()

    def intensite(self, point):
        return 1 / np.linalg.norm(self.position - point) ** 2