from primitive import Primitive

class Triangle(Primitive):
    def __init__(self, position, sommet1, sommet2, sommet3, couleur, materiau, max_profondeur = 1, ombre = True):
        super().__init__(position, couleur, materiau, max_profondeur, ombre)
        self.sommet1 = sommet1
        self.sommet2 = sommet2
        self.sommet3 = sommet3
        self.normale = (sommet2 - sommet1).produit_vectoriel(sommet3 - sommet1).normaliser()

    def intersection(self, origine, direction):
        denominateur = self.normale.dot(direction)
        if abs(denominateur) < 1e-6:
            return None
        t = (self.position - origine).dot(self.normale) / denominateur
        if t < 0:
            return None
        point = origine + direction * t
        u = (self.sommet2 - self.sommet1).produit_vectoriel(point - self.sommet1).dot(self.normale)
        v = (self.sommet3 - self.sommet2).produit_vectoriel(point - self.sommet2).dot(self.normale)
        w = (self.sommet1 - self.sommet3).produit_vectoriel(point - self.sommet3).dot(self.normale)
        if u >= 0 and v >= 0 and w >= 0:
            return t
        return None

    def normale(self, point):
        return self.normale