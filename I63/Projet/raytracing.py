import numpy as np
import time
import matplotlib.pyplot as plt # type: ignore
from PIL import Image # type: ignore

class Vecteur3D:
    '''
    Classe pour les vecteurs 3D
        x, y, z : float
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, autre):
        '''
        addition de deux vecteurs
        '''
        return Vecteur3D(self.x + autre.x, self.y + autre.y, self.z + autre.z)

    def soustraction(self, autre):
        '''
        Soustraction de deux vecteurs
        '''
        return Vecteur3D(self.x - autre.x, self.y - autre.y, self.z - autre.z)

    def multiplication(self, scalair):
        '''
        Multiplication d'un vecteur par un scalaire
        '''
        return Vecteur3D(self.x * scalair, self.y * scalair, self.z * scalair)

    def division(self, scalair):
        '''
        Division d'un vecteur par un scalaire
        '''
        return Vecteur3D(self.x / scalair, self.y / scalair, self.z / scalair)

    def __len__(self):
        '''
        Longueur du vecteur
        '''
        return 3

    def prod_scal(self, autre):
        '''
        Produit scalaire de deux vecteurs
        '''
        return self.x * autre.x + self.y * autre.y + self.z * autre.z

    def norme(self):
        '''
        Norme du vecteur
        '''
        return np.sqrt(self.prod_scal(self))

    def normalisation(self):
        '''
        Normalisation du vecteur
        '''
        return self.division(self.norme())
    
    def coord(self):
        '''
        Coordonnées du vecteur
        '''
        return self.x, self.y, self.z
    
    def as_list(self):
        '''
        Conversion du vecteur en liste
        '''
        return [self.x, self.y, self.z]

class Couleur:
    '''
    Classe pour les couleurs
        r, g, b : float
    '''
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __len__(self):
        '''
        Longueur de la couleur
        '''
        return 3
    
    def to_numpy(self):
        '''
        Conversion de la couleur en tableau numpy
        '''
        return np.array([self.r, self.g, self.b])
    
    def addition(self, autre):
        '''
        Addition de deux couleurs
        '''
        if isinstance(autre, Couleur):
            return Couleur(self.r + autre.r, self.g + autre.g, self.b + autre.b)
        elif isinstance(autre, (int, float)):
            return Couleur(self.r + autre, self.g + autre, self.b + autre)
    
    def multiplication(self, autre):
        '''
        Multiplication de deux couleurs
        '''
        if isinstance(autre, Couleur):
            return Couleur(self.r * autre.r, self.g * autre.g, self.b * autre.b)
        elif isinstance(autre, (int, float)):
            return Couleur(self.r * autre, self.g * autre, self.b * autre)
        

class Objet3D:
    '''
    Classe abstraite pour les objets 3D
        position : Vecteur3D
        couleur : Couleur
        diffuse_c : float (coefficient de diffusion)
        specular_c : float (coefficient de spéculaire)
        specular_k : float (exposant du spéculaire)
        reflection : float (coefficient de réflexion)
    '''
    def __init__(self, position, couleur, diffuse, specular, reflection):
        self.position = position
        self.couleur = couleur
        self.diffuse_c = diffuse
        self.specular_c = specular
        self.reflection = reflection


    def intersection(self, rayO, rayD):
        '''
        Calcul de l'intersection entre un rayon et un objet
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
        '''
        print('Méthode intersection à implémenter')

    def normale(self, M):
        '''
        Calcul de la normale à un point
            M : Vecteur3D (point)
        '''
        print('Méthode normale à implémenter')


class Sphere(Objet3D):
    '''
    Classe pour les sphères
        Parametres OBJET3D
        rayon : float
        n : float (indice de réfraction)
    '''
    def __init__(self, position, rayon, couleur, diffuse, specular, reflection, texture = None):
        super().__init__(position, couleur, diffuse, specular, reflection)
        self.rayon = rayon
        self.texture = texture
        
    def intersection(self, rayO, rayD):
        '''
        Calcul de l'intersection entre un rayon et une sphère
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
            a = 1 car rayD est normalisé (norme = 1) pas besoin de multiplier par a
        Retourne la distance entre l'origine du rayon et le point d'intersection
        '''
        OS = rayO.soustraction(self.position)                                        # Vecteur entre l'origine du rayon et le centre de la sphère
        b = 2 * rayD.prod_scal(OS)                                                # Coefficient du terme en t dans l'équation du second degré
        c = OS.prod_scal(OS) - self.rayon * self.rayon                            # Coefficient du terme constant dans l'équation du second degré
        delta = b * b - 4 * c                                               # Discriminant de l'équation du second degré
        if delta > 0:
            racine_delta = np.sqrt(delta)
            t1 = (-b - racine_delta) / 2
            t2 = (-b + racine_delta) / 2
            if t1 > 0:
                return t1
            elif t2 > 0:
                return t2
        elif delta == 0:
            return -b / 2
        return np.inf
    
    def normale(self, M):
        return (M.soustraction(self.position)).normalisation()

    def couleur_texture(self, M):
        '''
        Calcul de la couleur d'un point sur la sphère (en utilisant la bilinéarisation pour rendre la texture plus réaliste)
            M : Vecteur3D (point d'intersection)
        Retourne la couleur du point
        '''
        if self.texture is None:    # Si pas de texture définie, on retourne la couleur de la sphère
            return self.couleur

        M = M.soustraction(self.position).normalisation()   # Normalisation du point d'intersection par rapport au centre de la sphère

        angle_rotation = np.pi / 4  # Angle de rotation pour la texture (45°)

        u = (0.5 + np.arctan2(M.z, M.x) + angle_rotation) / (2 * np.pi) # Coordonnée u de la texture
        v = 0.5 - np.arcsin(M.y) / np.pi                            # Coordonnée v de la texture

        x, y = self.texture.size    # Dimensions de la texture
        u = min(max(u, 0), 1) * (x - 1) # Coordonnée u de la texture (entre 0 et x - 1)
        v = min(max(v, 0), 1) * (y - 1) # Coordonnée v de la texture (entre 0 et y - 1)
        i = min(int(u), x - 2)  # Partie entière de u
        j = min(int(v), y - 2)  # Partie entière de v
        u_ratio = u - i        # Partie décimale de u
        v_ratio = v - j       # Partie décimale de v
        u_opposite = 1 - u_ratio    # Partie opposée de u
        v_opposite = 1 - v_ratio    # Partie opposée de v

        p1 = self.texture.getpixel((i, j))  # Pixel en haut à gauche
        p2 = self.texture.getpixel((i + 1, j))  # Pixel en haut à droite
        p3 = self.texture.getpixel((i, j + 1))  # Pixel en bas à gauche
        p4 = self.texture.getpixel((i + 1, j + 1))  # Pixel en bas à droite

        # Interpolation bilinéaire
        r = (p1[0]*u_opposite + p2[0]*u_ratio)*v_opposite + (p3[0]*u_opposite + p4[0]*u_ratio)*v_ratio  # Couleur rouge
        g = (p1[1]*u_opposite + p2[1]*u_ratio)*v_opposite + (p3[1]*u_opposite + p4[1]*u_ratio)*v_ratio  # Couleur verte
        b = (p1[2]*u_opposite + p2[2]*u_ratio)*v_opposite + (p3[2]*u_opposite + p4[2]*u_ratio)*v_ratio  # Couleur bleue

        return Couleur(r / 255, g / 255, b / 255)   # Retourne la couleur normalisée


class Plan(Objet3D):
    '''
    Classe pour les plans
        Parametres OBJET3D
        normal : Vecteur3D
    '''
    def __init__(self, position, normal, couleur, diffuse, specular, reflection, texture = None):
        super().__init__(position, couleur, diffuse, specular, reflection)
        self.normal = normal.normalisation()
        self.texture = texture

    def intersection(self, rayO, rayD):
        '''
        Calcul de l'intersection entre un rayon et un plan
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
        Retourne la distance entre l'origine du rayon et le point d'intersection
        '''
        denominateur = rayD.prod_scal(self.normal)                            # Produit scalaire entre la direction du rayon et la normale du plan
        if np.abs(denominateur) < 1e-10:                                # Si le dénominateur est proche de 0, le rayon est parallèle au plan
            return np.inf                                               # Pas d'intersection
        d = (self.position.soustraction(rayO).prod_scal(self.normal)) / denominateur   # Distance entre l'origine du rayon et le point d'intersection
        if d < 0:
            return np.inf                                               # Pas d'intersection si la distance est négative
        return d
    
    def normale(self, M):
        '''
        Calcul de la normale à un point
            M : inutilisé car la normale est constante
        '''
        return self.normal
    
    def get_uv(self, M):
        '''
        Calcul des coordonnées uv du point d'intersection
            M : Vecteur3D (point d'intersection)
        Retourne les coordonnées uv
        '''
        u = (M.x - np.floor(M.x)) # Coordonnée u
        v = (M.z - np.floor(M.z)) # Coordonnée v
        return u, v
    
    def couleur_texture(self, M):
        '''
        Calcul de la couleur d'un point sur le plan (en utilisant la texture)
            M : Vecteur3D (point d'intersection)
        Retourne la couleur du point
        '''
        if self.texture is None:
            return self.couleur
        
        u, v = self.get_uv(M)   # Coordonnées uv du point d'intersection
        x, y = self.texture.size    # Dimensions de la texture
        u = min(max(u, 0), 1) * (x - 1) # Coordonnée u de la texture (entre 0 et x - 1)
        v = min(max(v, 0), 1) * (y - 1) # Coordonnée v de la texture (entre 0 et y - 1)
        i = min(int(u), x - 2)  # Partie entière de u
        j = min(int(v), y - 2)  # Partie entière de v
        u_ratio = u - i        # Partie décimale de u
        v_ratio = v - j       # Partie décimale de v
        u_opposite = 1 - u_ratio    # Partie opposée de u
        v_opposite = 1 - v_ratio    # Partie opposée de v
        p1 = self.texture.getpixel((i, j))  # Pixel en haut à gauche
        p2 = self.texture.getpixel((i + 1, j))  # Pixel en haut à droite
        p3 = self.texture.getpixel((i, j + 1))  # Pixel en bas à gauche
        p4 = self.texture.getpixel((i + 1, j + 1))  # Pixel en bas à droite
        # Interpolation bilinéaire
        if isinstance(p1, int):
            r = (p1*u_opposite + p2*u_ratio)*v_opposite + (p3*u_opposite + p4*u_ratio)*v_ratio
            g = (p1*u_opposite + p2*u_ratio)*v_opposite + (p3*u_opposite + p4*u_ratio)*v_ratio
            b = (p1*u_opposite + p2*u_ratio)*v_opposite + (p3*u_opposite + p4*u_ratio)*v_ratio
        else:
            r = (p1[0]*u_opposite + p2[0]*u_ratio)*v_opposite + (p3[0]*u_opposite + p4[0]*u_ratio)*v_ratio
            g = (p1[1]*u_opposite + p2[1]*u_ratio)*v_opposite + (p3[1]*u_opposite + p4[1]*u_ratio)*v_ratio
            b = (p1[2]*u_opposite + p2[2]*u_ratio)*v_opposite + (p3[2]*u_opposite + p4[2]*u_ratio)*v_ratio
        return Couleur(r / 255, g / 255, b / 255)   # Retourne la couleur normalisée

        
class Lumiere:
    '''
    Classe pour les lumières
        position : Vecteur3D
        couleur : Couleur
    '''
    def __init__(self, position, couleur):
        self.position = position
        self.couleur = couleur

class Camera:
    '''
    Classe pour la caméra
        position : Vecteur3D
        direction : Vecteur3D
    '''
    def __init__(self, position, direction, distance_focale):
        self.position = position
        self.direction = direction
        self.distance_focale = distance_focale

class Scene:
    '''
    Classe pour les scènes
        dimensions : tuple (largeur, hauteur)
        objets : list[Objet3D]
        lumiere : list[Lumiere]
        camera : Camera
        ambient : float (entre 0 et 1)
        profondeur_max : int
    '''
    def __init__(self, dimensions, objets, lumieres, camera, ambiante, profondeur_max):
        self.dimensions = dimensions
        self.objets = objets
        self.lumieres = lumieres
        self.camera = camera
        self.ambiante = ambiante
        self.profondeur_max = profondeur_max

    def ajouter_objet(self, objet):
        '''
        Ajout d'un objet à la scène
        '''
        self.objets.append(objet)

    def ajouter_lumiere(self, lumiere):
        '''
        Ajout d'une lumière à la scène
        '''
        self.lumieres.append(lumiere)

    def intersect(self, rayO, rayD, objet):
        '''
        Calcul de l'intersection entre un rayon et un objet
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
            objet : Objet3D
        Retourne la distance entre l'origine du rayon et le point d'intersection
        '''
        if hasattr(objet, 'n'):
            return objet.intersection(rayO, rayD)
        else:
            return objet.intersection(rayO, rayD)

    def get_color(self, objet, M):
        '''
        Calcul de la couleur d'un objet
            objet : Objet3D
            M : Vecteur3D (point d'intersection)
        Retourne la couleur de l'objet
        '''
        couleur = objet.couleur
        if isinstance(couleur, Couleur):    # Si la couleur est une couleur
            return couleur
        elif callable(couleur):             # Si la couleur est une fonction
            return couleur(M)
        
    def intersection_plus_proche(self, rayO, rayD):
        '''
        Calcul de l'intersection la plus proche entre un rayon et un objet
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
        Retourne la distance entre l'origine du rayon et le point d'intersection et l'indice de l'objet intersecté
        '''
        t = np.inf
        obj_idx = 0
        for i, objet in enumerate(self.objets): # Pour chaque objet de la scène
            t_obj = self.intersect(rayO, rayD, objet)   # Calcul de l'intersection entre le rayon et l'objet
            if t_obj < t:   # Si la distance est inférieure à la distance minimale
                t, obj_idx = t_obj, i   # Mise à jour de la distance minimale et de l'indice de l'objet
        return t, obj_idx
    
    def illumination(self, M, N, couleur, objet, O, obj_idx):
        '''
        Calcul de l'illumination d'un objet
            M : Vecteur3D (point d'intersection)
            N : Vecteur3D (normale)
            couleur : Couleur
            objet : Objet3D
            O : Vecteur3D (direction du rayon)
            obj_idx : int (indice de l'objet)
        Retourne la couleur de l'objet
        '''
        col_ray = Couleur(self.ambiante, self.ambiante, self.ambiante)  # Couleur du rayon (couleur ambiante)
        for lumiere in self.lumieres:   # Pour chaque lumière de la scène
            L = (lumiere.position.soustraction(M)).normalisation()  # Direction de la lumière
            l = [self.intersect(M.addition(N.multiplication(0.000001)), L, obj) for k, obj in enumerate(self.objets) if k != obj_idx]   # Intersection entre le point d'intersection et la lumière
            if l and min(l) < np.inf:   # Si l'intersection est plus proche que la lumière
                intensite_ombre = 0.3   # Intensité de l'ombre
                couleur = couleur.multiplication(intensite_ombre)  # Couleur de l'ombre
            l_diffus = max(N.prod_scal(L), 0)   # Coefficient de diffusion
            if isinstance(couleur, tuple):  # Si la couleur est un tuple
                col_ray = col_ray.addition(Couleur(*[l_diffus * c for c in couleur]))   # Ajout de la couleur du rayon à la couleur ambiante
            else:
                col_ray = col_ray.addition(couleur.multiplication(l_diffus * objet.diffuse_c))  # Ajout de la couleur du rayon à la couleur ambiante
            col_ray = col_ray.addition(lumiere.couleur.multiplication(l_diffus * objet.specular_c * max(N.prod_scal((L.addition(O)).normalisation()), 0) ** 100))   # Ajout de la couleur spéculaire du rayon à la couleur ambiante
        return col_ray

    def rayon_trace(self, rayO, rayD):
        '''
        Calcul du rayon de trace
            rayO : Vecteur3D (origine du rayon)
            rayD : Vecteur3D (direction du rayon)
        Retourne l'objet intersecté, le point d'intersection, la normale et la couleur du rayon
        '''
        t, obj_idx = self.intersection_plus_proche(rayO, rayD)  # Calcul de l'intersection la plus proche
        if t == np.inf: # Si pas d'intersection
            return None
        objet = self.objets[obj_idx]    # Objet intersecté
        M = rayO.addition(rayD.multiplication(t))   # Point d'intersection
        N = objet.normale(M)    # Normale
        if hasattr(objet, 'texture'):   # Si l'objet a une texture, on utilise la couleur de la texture
            couleur = objet.couleur_texture(M)
        else:
            couleur = self.get_color(objet, M)  # Sinon, on utilise la couleur de l'objet
        O = (self.camera.position.soustraction(M)).normalisation()  # Direction du rayon
        col_ray = self.illumination(M, N, couleur, objet, O, obj_idx)   # Couleur du rayon
            
        return objet, M, N, col_ray # Objet intersecté, point d'intersection, normale et couleur
    
    def couleur_pixel(self, x, y):
        '''
        Calcul de la couleur d'un pixel
            x : float
            y : float
        Retourne la couleur du pixel
        '''
        col = Couleur(0, 0, 0)  # Couleur du pixel
        Q = Vecteur3D(x, y, -self.camera.distance_focale)  # Coordonnées du pixel
        D = (Q.soustraction(self.camera.position)).normalisation()   # Direction du rayon en utilisant la position de la caméra ()
        profondeur = 0
        rayO, rayD = self.camera.position, D    # RayO : origine du rayon, RayD : direction du rayon
        reflection = 1                        # Réflexion du rayon (1 = pas de réflexion)
        continu = True
        while profondeur < self.profondeur_max and continu: # Tant que la profondeur est inférieure à la profondeur maximale
            trace = self.rayon_trace(rayO, rayD)    # Calcul du rayon de trace (objet intersecté, point d'intersection, normale et couleur)
            if not trace:   # Si pas d'intersection
                continu = False    # Arrêt de la boucle car pas d'objet intersecté donc inutile de continuer
            else:
                objet, M, N, col_ray = trace    # Objet intersecté, point d'intersection, normale et couleur
                rayO, rayD = M.addition(N.multiplication(0.0001)), rayD.soustraction(N.multiplication(2 * N.prod_scal(rayD))) # Réflexion du rayon
                profondeur += 1
                col = col.addition(col_ray.multiplication(reflection))  # Ajout de la couleur du rayon à la couleur du pixel
                reflection *= objet.reflection  # Réflexion de l'objet
        return col

    def construire_image(self):
        '''
        Construction de l'image
        Retourne l'image de la scène
        '''
        largeur, hauteur = self.dimensions  # Dimensions de l'image
        coords_ecran = (-largeur / hauteur, -1, largeur / hauteur, 1)   # Coordonnées de l'écran de la caméra (normalisé)
        img = np.zeros((hauteur, largeur, 3))                        # Image de la scène
        for i, x in enumerate(np.linspace(coords_ecran[0], coords_ecran[2], largeur)):  # Pour chaque pixel de l'image (en x)
            for j, y in enumerate(np.linspace(coords_ecran[1], coords_ecran[3], hauteur)):  # Pour chaque pixel de l'image (en y)
                col = self.couleur_pixel(x, y)  # Calcul de la couleur du pixel
                img[hauteur - j - 1, i, :] = np.clip(col.to_numpy(), 0, 1)  # Ajout de la couleur du pixel à l'image (inversion verticale)
        return img

# Paramètres de la scène
largeur = 1280
hauteur = 1024
profondeur_max = 15

start = time.time()

# Création de la caméra
camera = Camera(Vecteur3D(0, 0, -1), Vecteur3D(0, 0, 1), 2)

# Création de la scène
scene = Scene((largeur, hauteur), [], [], camera, 0.1, profondeur_max)

# Ajout de la lumière
scene.ajouter_lumiere(Lumiere(Vecteur3D(-5, 8, 1), Couleur(1, 1, 1)))


# Création des objets
texture = Image.open('8081_earthmap4k.jpg')  # Texture de la sphère
sphere1 = Sphere(Vecteur3D(0, 0, -4), 0.6, Couleur(1, 1, 1), 1, 0, 0, texture)
# Deuxieme sphere blanche à droit de la première
sphere2 = Sphere(Vecteur3D(1.7, 0, -4), 0.6, Couleur(1, 1, 1), 0.5, 0.5, 0.5)
# Troisième sphere blanche à gauche de la première
texture4 = Image.open('oak.jpg')
sphere3 = Sphere(Vecteur3D(-1.7, 0, -4), 0.6, Couleur(1, 1, 1), 0.9, 0.1, 0, texture4)


# plan blanc en dessous des sphères
texture2 = Image.open('damier.jpg')  # Texture du plan
plan1 = Plan(Vecteur3D(0, -0.61, 0), Vecteur3D(0, 1, 0), Couleur(1, 1, 1), 0.5, 0.5, 1, texture2)

# mur blanc au fond de la scène jusqu'aux limites de l'écran
plan2 = Plan(Vecteur3D(0, 0, -9), Vecteur3D(0, 0, 1), Couleur(1, 1, 1), 0.5, 0.5, 0.5)



# Ajout des objets à la scène
scene.ajouter_objet(sphere1)
scene.ajouter_objet(sphere2)
scene.ajouter_objet(sphere3)
scene.ajouter_objet(plan1)
scene.ajouter_objet(plan2)

# Rendu de l'image
img = scene.construire_image()

# Sauvegarde de l'image
plt.imsave('image_final.png', img)

print('Temps de rendu :', time.time() - start, 's')