#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

###############################################################
# variables globales
annee, jour , lune, rev_lune= 0, 0, 0, 0
quadric = None
cam_x, cam_y, cam_z = 0.0, 0.0, 5.0

###############################################################
#

def init():
    '''
    Fonction qui initialise les paramètres
    '''
    global quadric
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DITHER)
    glEnable(GL_DEPTH_TEST) # Pour utiliser le DEPTH
    glEnable(GL_COLOR_MATERIAL) # Pour utiliser les couleurs
    glEnable(GL_LINE_SMOOTH)    # Pour utiliser les lignes lisses
    glEnable(GL_LIGHTING)   # Pour utiliser la lumière
    glEnable(GL_LIGHT0)  # Pour utiliser la lumière
    glEnable(GL_BLEND)  # Pour utiliser la transparence
    glShadeModel(GL_SMOOTH) # Pour utiliser les ombrages
    quadric = gluNewQuadric()   # Pour utiliser les quadriques
    gluQuadricDrawStyle(quadric, GLU_FILL)

def display():
    '''
    Fonction qui dessine les objets
    '''
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()

    glTranslatef(cam_x, cam_y, cam_x)

    sun_emission = [1.0, 1.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, sun_emission)   # Emission de la lumière
    gluSphere(quadric, 1.0, 20, 16)   # Dessine le soleil
    light_position = [0.0, 0.0, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)    # Position de la lumière
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])   # Fin de l'émission de la lumière

    glRotatef(annee, 0.0, 1.0, 0.0)  # Rotation de la terre (année)
    glTranslatef(2.0, 0.0, 0.0) # Translation de la terre
    glRotatef(jour, 0.0, 1.0, 0.0)  # Rotation de la terre (jour)
    glColor4f(0.0, 0.0, 1.0, 1.0)   # Couleur de la terre
    gluSphere(quadric, 0.2, 10, 8)  # Dessine la terre

    glRotatef(rev_lune, 0.0, 1.0, 0.0)  # Rotation de la lune (révolution)
    glTranslatef(0.5, 0.0, 0.0)  # Translation de la lune
    glRotatef(lune, 0.0, 1.0, 0.0)  # Rotation de la lune (jour)
    glColor4f(0.5, 0.5, 0.5, 1.0)   # Couleur de la lune
    gluSphere(quadric, 0.1, 5, 4)   # Dessine la lune

    glPopMatrix()

    glutSwapBuffers()

def reshape(width, height):
    '''
    Fonction qui gère le redimensionnement de la windows
    '''
    glViewport(0, 0, width, height)
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)   # Position de la caméra
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(20, width/height, 1, 200)   # Perspective
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    '''
    Fonction qui gère les évènements clavier
    '''
    global jour, annee, lune, rev_lune, cam_x, cam_y, cam_z
    key = key.decode('utf-8')
    if key == 'j':
        jour = (jour + 10) % 360
    elif key == 'a':
        annee = (annee + 5) % 360
    elif key == 'r':
        for i in range(900):
            jour = (jour + 5/360.25) % 360
            annee = (annee + 5) % 360
            lune = (lune + 40) % 360
            rev_lune = (rev_lune + 40) % 360
            display()
    elif key == 'z':
        cam_x = cam_x + 0.1
    elif key == 's':
        cam_x = cam_x - 0.1
    elif key == 'q':
        cam_z = cam_z + 0.1
    elif key == 'd':
        cam_z = cam_z - 0.1
    elif key == 'w':
        cam_y = cam_y + 0.1
    elif key == 'x':
        cam_y = cam_y - 0.1
    elif key == '\033':
        # sys.exit( )  # Exception ignored
        glutLeaveMainLoop()
    glutPostRedisplay()  # indispensable en Python

###############################################################
# MAIN

'''
Initialise la windows et lance la boucle d'évènement
'''

glutInit()  # Initialise la librairie GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)    # Initialise le mode display en selectionnant un double buffer, le mode RGBA et DEPTH pour la profondeur des objets

glutCreateWindow('planet')  # Cree un Top-Level windows qui porte le nom "planet"
glutReshapeWindow(1000,1000)  # Taille de la windows

'''
Callback
'''
glutReshapeFunc(reshape)    # Callback pour modifier la taille de la windows
glutDisplayFunc(display)    # Callback pour la windows présente (Fonction très importante)
glutKeyboardFunc(keyboard)  # Callback pour activer le clavier pour la windows présente (touches normales caractères ASCII)

init()

glutMainLoop()