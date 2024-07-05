import numpy as np
from vecteurs import Vecteur3D
from primitive import Primitive
from plan import Plan

class Parallelipipede(Primitive):
    def __init__(self, position, longueur, largeur, hauteur, couleur, materiau, max_profondeur = 1, ombre = True):
        super().__init__(position, couleur, materiau, max_profondeur, ombre)
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.plans = []
        self.plans.append(Plan(position, Vecteur3D(0, 0, 1), couleur, materiau, max_profondeur, ombre))
        self.plans.append(Plan(position + Vecteur3D(longueur, 0, 0), Vecteur3D(0, 0, 1), couleur, materiau, max_profondeur, ombre))
        self.plans.append(Plan(position, Vecteur3D(0, 1, 0), couleur, materiau, max_profondeur, ombre))
        self.plans.append(Plan(position + Vecteur3D(0, largeur, 0), Vecteur3D(0, 1, 0), couleur, materiau, max_profondeur, ombre))
        self.plans.append(Plan(position, Vecteur3D(1, 0, 0), couleur, materiau, max_profondeur, ombre))
        self.plans.append(Plan(position + Vecteur3D(0, 0, hauteur), Vecteur3D(1, 0, 0), couleur, materiau, max_profondeur, ombre))

    def intersection(self, origine, direction):
        t_min = None
        for plan in self.plans:
            t = plan.intersection(origine, direction)
            if t is not None:
                if t_min is None or t < t_min:
                    t_min = t
        return t_min

    def normale(self, point):
        for plan in self.plans:
            if plan.intersection(point, plan.normale) is not None:
                return plan.normale
        raise ValueError("No normale found")