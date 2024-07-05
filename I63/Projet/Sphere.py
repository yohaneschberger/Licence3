import numpy as np
from primitive import Primitive

class Sphere(Primitive):
    def __init__(self, position, rayon, couleur, materiau, max_profondeur = 1, ombre = True):
        super().__init__(position, couleur, materiau, max_profondeur, ombre)
        self.rayon = rayon

    def intersection(self, origine, direction):
        L = self.position - origine
        tca = L.dot(direction)
        d2 = L.dot(L) - tca * tca
        if d2 > self.rayon * self.rayon:
            return None
        thc = np.sqrt(self.rayon * self.rayon - d2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        return t0
    
    def normale(self, point):
        return (point - self.position).normalise()
