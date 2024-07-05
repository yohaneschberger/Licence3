import time
import matplotlib.pyplot as plt
from PIL import Image
import Vecteur3D as lVecteur
import Couleur as lCouleur
import Sphere as lSphere
import Plan as lPlan
import Lumiere as lLumiere
import Camera as lCamera
import Scene as lScene


# Paramètres de la scène
largeur = 1280
hauteur = 1024
profondeur_max = 15

start = time.time()

# Création de la caméra
camera = lCamera.Camera(lVecteur.Vecteur3D(0, 0, -1), lVecteur.Vecteur3D(0, 0, 1), 2)

# Création de la scène
scene = lScene.Scene((largeur, hauteur), [], [], camera, 0.1, profondeur_max)

# Ajout de la lumière
scene.ajouter_lumiere(lLumiere.Lumiere(lVecteur.Vecteur3D(-5, 8, 1), lCouleur.Couleur(1, 1, 1)))


# Création des objets
texture = Image.open('8081_earthmap4k.jpg')  # Texture de la sphère
sphere1 = lSphere.Sphere(lVecteur.Vecteur3D(0, 0, -4), 0.6, lCouleur.Couleur(1, 1, 1), 1, 0, 0, texture)
# Deuxieme sphere blanche à droit de la première
sphere2 = lSphere.Sphere(lVecteur.Vecteur3D(1.7, 0, -4), 0.6, lCouleur.Couleur(1, 1, 1), 0.5, 0.5, 0.5)
# Troisième sphere blanche à gauche de la première
texture4 = Image.open('oak.jpg')
sphere3 = lSphere.Sphere(lVecteur.Vecteur3D(-1.7, 0, -4), 0.6, lCouleur.Couleur(1, 1, 1), 0.9, 0.1, 0, texture4)


# plan blanc en dessous des sphères
texture2 = Image.open('damier.jpg')  # Texture du plan
plan1 = lPlan.Plan(lVecteur.Vecteur3D(0, -0.61, 0), lVecteur.Vecteur3D(0, 1, 0), lCouleur.Couleur(1, 1, 1), 0.5, 0.5, 1, texture2)

# mur blanc au fond de la scène jusqu'aux limites de l'écran
plan2 = lPlan.Plan(lVecteur.Vecteur3D(0, 0, -9), lVecteur.Vecteur3D(0, 0, 1), lCouleur.Couleur(1, 1, 1), 0.5, 0.5, 0.5)



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