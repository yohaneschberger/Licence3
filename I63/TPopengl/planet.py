#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
# from Image import open
from PIL import Image
import numpy as np

###############################################################
# variables globales
year, day = 0, 0  # Terre
luna, periode = 0, 0  # Lune
quadric = None
SOLEIL, TERRE, ATERRE, LUNE = 1, 2, 3, 4  # ID astre, planete, satellite
texture_planete = [None for i in range(5)]
cam_x, cam_y, cam_z, cam_rx, cam_ry = 0.0, 0.0, 5.0, 0.0, 0.0 # Position de la caméra

###############################################################
# chargement des textures

def LoadTexture(filename, ident):
    global texture_planete
    image = Image.open(filename)  # retourne une PIL.image
    
    ix = image.size[0]
    iy = image.size[1]
    # image = image.tostring("raw", "RGBX", 0, -1)
    image = image.tobytes("raw", "RGBX", 0, -1)
    
    # 2d texture (x and y size)
    # BUG (?)
    #glBindTexture(GL_TEXTURE_2D, glGenTextures(1, texture_planete[ident]))
    texture_planete[ident] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, int(texture_planete[ident]))

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # commente car alpha blinding (cf. atmosphere)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

###############################################################
# creation des composants du systeme

def CreerPlanete(rayon):
    ambient = (0.1, 0.1, 0.1, 1.0)
    diffuse = (0.8, 0.8, 0.8, 1.0)
    Black = (0.0, 0.0, 0.0, 1.0)
    sph1 = gluNewQuadric()

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Black)
    glMaterialfv(GL_FRONT, GL_EMISSION, ambient)
    glMaterialf(GL_FRONT, GL_SHININESS, 0.0)

    gluQuadricDrawStyle(sph1, GLU_FILL)
    gluQuadricNormals(sph1, GLU_SMOOTH)
    gluQuadricTexture(sph1, GL_TRUE)
    gluSphere(sph1, rayon, 100, 80)

def CreerSoleil(rayon):
    ambient = (1.0, 1.0, 0.0, 1.0)  # Jaune
    diffuse = (1.0, 1.0, 0.0, 1.0)  # Jaune
    Black = (0.0, 0.0, 0.0, 1.0)
    sph1 = gluNewQuadric()

    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient) # Matériau de l'astre (ambiant)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse) # Matériau de l'astre (diffus)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Black)  # Matériau de l'astre (spéculaire)
    glMaterialfv(GL_FRONT, GL_EMISSION, ambient)    # Matériau de l'astre (émission)
    glMaterialf(GL_FRONT, GL_SHININESS, 0.0)    # Matériau de l'astre (brillance)

    gluQuadricDrawStyle(sph1, GLU_FILL)
    gluQuadricNormals(sph1, GLU_SMOOTH)
    gluQuadricTexture(sph1, GL_TRUE)
    gluSphere(sph1, rayon, 100, 80)

###############################################################

# affichage

def display_sun():
    global year, day, luna, periode
    init_texture("sun.bmp", SOLEIL)
    glPushMatrix()
    glTranslatef(cam_x, cam_y, cam_x)
    CreerSoleil(1.0)
    glPopMatrix()

def display_earth():
    global year, day, luna, periode
    init_texture("earth.bmp", TERRE)
    glPushMatrix()
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(3.0, 0.0, 0.0)  # Translate par rapport au Soleil
    glRotatef(day, 0.23, 1.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    CreerPlanete(0.2)
    glPopMatrix()

def display_atmosphere():
    global year, day, luna, periode
    init_texture("earthcld.bmp", ATERRE)
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(1.0, 1.0, 1.0, 0.2) # Couleur de l'atmosphère transparente (80% de transparence)
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(3.0, 0.0, 0.0)  # Translate par rapport au Soleil
    glRotatef(day, 0.0, 1.0, 0.0)
    CreerPlanete(0.22)  # Atmosphère légèrement plus grande que la planète
    glDisable(GL_BLEND)
    glPopMatrix()

def display_moon():
    global year, day, luna, periode
    init_texture("moon.bmp", LUNE)
    glPushMatrix()
    glRotatef(year, 0.0, 1.0, 0.0)
    glTranslatef(3.0, 0.0, 0.0)  # Translate par rapport au Soleil
    glRotatef(luna, 0.0, 1.0, 0.0)
    glTranslatef(0.5, 0.0, 0.0)  # Translate par rapport à la Terre
    glRotatef(periode, 0.0, 1.0, 0.0)
    CreerPlanete(0.05)
    glPopMatrix()

###############################################################

def init_texture(image, ident):
    LoadTexture(image, ident)

def init():
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST) # Pour utiliser le DEPTH
    glDepthFunc(GL_LEQUAL)  # Type de test de profondeur
    glEnable(GL_LIGHTING)   # Pour utiliser la lumière
    glEnable(GL_LIGHT0)     # Pour utiliser la lumière
    glEnable(GL_COLOR_MATERIAL) # Pour utiliser les couleurs
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)   # Correction de la perspective
    glShadeModel(GL_SMOOTH) # Pour utiliser les ombrages

def display():
    # Effacer le buffer de couleur et de profondeur
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Réinitialiser la matrice de modèle-vue
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(cam_x, cam_y, cam_z, 0, 0, 0, 0, 1, 0)

    glTranslatef(cam_x, cam_y, cam_x)
    glRotatef(cam_rx, 0.0, 1.0, 0.0)
    glRotatef(cam_ry, 1.0, 0.0, 0.0)

    # Dessiner le soleil
    glPushMatrix()
    display_sun()
    glPopMatrix()

    light_position = [0.0, 0.0, 0.0, 1.0]  # La position de la lumière est la même que celle du soleil
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)  # Position de la lumière

    # Dessiner la terre
    glPushMatrix()
    display_earth()
    glPopMatrix()

    # Dessiner l'atmosphère
    glPushMatrix()
    display_atmosphere()
    glPopMatrix()

    # Dessiner la lune
    glPushMatrix()
    display_moon()
    glPopMatrix()

    # Échanger les buffers
    glutSwapBuffers()

def reshape(width, height):
    '''
    Fonction qui gère le redimensionnement de la windows
    '''
    ar = width / height # Ratio de l'écran

    glViewport(0, 0, width, height) # Définit la zone d'affichage
    glMatrixMode(GL_PROJECTION) # Définit la matrice de projection
    glLoadIdentity()    # Réinitialise la matrice de projection
    glFrustum(-ar, ar, -1.0, 1.0, 1.5, 20.0)   # Frustum
    glMatrixMode(GL_MODELVIEW)  # Définit la matrice de modèle-vue
    glLoadIdentity()

def keyboard(key, x, y):
    global cam_x, cam_y, cam_z, cam_rx, cam_ry, day, year, luna, periode
    key = key.decode('utf-8')
    if key == 'b':
        day = (day + 5/360.25) % 360  # Rotation de la Terre sur elle-même
        year = (year + 5) % 360  # Rotation de la Terre autour du Soleil
        luna = (luna + 40) % 360  # Rotation de la Lune autour de la Terre
        periode = (periode + 40) % 360  # Rotation de la Lune autour de la Terre
    elif key == 'z':
        cam_y = cam_y + 0.1
    elif key == 's':
        cam_y = cam_y - 0.1
    elif key == 'q':
        cam_x = cam_x + 0.1
    elif key == 'd':
        cam_x = cam_x - 0.1
    elif key == 'w':
        cam_z = cam_z + 0.1 # Zoom avant
    elif key == 'x':
        cam_z = cam_z - 0.1 # Zoom arrière
    elif key == 'a':
        cam_rx = cam_rx + 1.0 # Rotation à gauche
    elif key == 'e':
        cam_rx = cam_rx - 1.0 # Rotation à droite
    elif key == 'r':
        cam_ry = cam_ry + 1.0
    elif key == 't':
        cam_ry = cam_ry - 1.0
    elif key == '\033':
        # sys.exit( )  # Exception ignored
        glutLeaveMainLoop()
    glutPostRedisplay()

###############################################################
# MAIN

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)    # Initialise le mode display en selectionnant un double buffer, le mode RGBA et DEPTH pour la profondeur des objets

glutCreateWindow('planet')  # Cree un Top-Level windows qui porte le nom "planet"
glutReshapeWindow(1400,1000)  # Taille de la windows

'''
Callback
'''
glutReshapeFunc(reshape)    # Callback pour modifier la taille de la windows 
glutDisplayFunc(display)    # Callback pour la windows présente (Fonction très importante)
glutKeyboardFunc(keyboard)  # Callback pour activer le clavier pour la windows présente (touches normales caractères ASCII)

init()  # Initialisation des paramètres

glutMainLoop()