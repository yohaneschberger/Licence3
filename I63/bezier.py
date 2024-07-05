import cng
from math import comb  # Importation de la fonction comb pour calculer les coefficients binomiaux

###############################################################

# Constantes

TOLERANCE = 10  # Tolérance pour le clic
points_controls = []    # Liste des points de contrôle

###############################################################

def clique(point, mouse_x, mouse_y):
    '''
    Retourne True si le point est cliqué, False sinon.
    '''
    return abs(point[0] - mouse_x) < TOLERANCE and abs(point[1] - mouse_y) < TOLERANCE  # On vérifie si le point est cliqué

def maj_position(mouse_x, mouse_y):
    '''
    Retourne les coordonnées du point mis à jour.
    '''
    return (mouse_x, mouse_y)

def bezier(t):
    '''
    Retourne les coordonnées du point de la courbe de Bézier correspondant au paramètre t.
    '''
    x = 0
    y = 0
    n = len(points_controls) - 1
    for i, point in enumerate(points_controls):  # On calcule les coordonnées du point de la courbe de Bézier
        x += comb(n, i) * (1 - t)**(n - i) * t**i * point[0]    # On utilise la formule de Bézier
        y += comb(n, i) * (1 - t)**(n - i) * t**i * point[1]
    return x, y

def clique_souris():
    '''
    Ajoute un point de contrôle si la souris est cliquée.
    '''
    if len(points_controls) < 4:    # On ne peut pas dessiner une courbe de Bézier avec moins de 4 points de contrôle
        mouse_x = cng.get_mouse_x()
        mouse_y = cng.get_mouse_y()
        for i, point in enumerate(points_controls):   # On vérifie si un point de contrôle est cliqué
            if clique(point, mouse_x, mouse_y):  # Si un point est cliqué, on le met à jour
                points_controls[i] = maj_position(mouse_x, mouse_y)
        else:   # Si aucun point n'est cliqué, on en ajoute un
            points_controls.append((mouse_x, mouse_y))
        dessiner_bezier(points_controls)

def dessiner_bezier(points_controls):
    '''
    Dessine la courbe de Bézier.
    '''
    cng.clear_screen()  # On efface l'écran
    if len(points_controls) > 3:
        cng.current_color("red")    # On choisit la couleur rouge
        for t in range(0, 1000):    # On trace la courbe de Bézier
            t = t / 1000    # On normalise t
            x, y = bezier(t)    
            cng.point(x, y)
    for point in points_controls:   # On trace les points de contrôle
        cng.disc(point[0], point[1], 5)

###############################################################

cng.init_window('Bezier', 800, 800)   # Initialisation de la fenêtre

cng.assoc_button(1, clique_souris)  # On associe la fonction clique_souris au clic gauche

cng.main_loop() # Boucle principale

###############################################################

