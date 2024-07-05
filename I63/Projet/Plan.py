import numpy as np
from primitive import Primitive

class Plan(Primitive):
    def __init__(self, position, normale, couleur, materiau, max_profondeur = 1, ombre = True):
        super().__init__(position, couleur, materiau, max_profondeur, ombre)
        self.normale = normale

    def intersection(self, origine, direction):
        denominateur = self.normale.dot(direction)
        if abs(denominateur) < 1e-6:
            return None
        t = (self.position - origine).dot(self.normale) / denominateur
        if t < 0:
            return None
        return t

    def normale(self, point):
        return self.normale