from random import randint
import matplotlib.pyplot as plt
import numpy as np
import csv

# Définit une matrice 8x8 avec des 0
def create_blank_matrix():
    return [[0 for i in range(8)] for j in range(8)]

def ligne_verticale(M):
    '''
    Ajoute une ligne verticale à la matrice
    '''
    for i in range(8):
        M[i][3] = 1 if randint(0, 10) % 2 == 0 else M[i][3]
        M[i][4] = 1 if randint(0, 10) % 2 == 0 else M[i][4]
    return M

def ligne_horizontale(M):
    '''
    Ajoute une ligne horizontale à la matrice
    '''
    for i in range(8):
        M[3][i] = 1 if randint(0, 10) % 2 == 0 else M[3][i]
        M[4][i] = 1 if randint(0, 10) % 2 == 0 else M[4][i]
    return M

def centre(M):
    '''
    Ajoute un centre à la matrice
    '''
    for i in range(2, 6):
        for j in range(2, 6):
            M[i][j] = 1 if randint(0, 10) % 2 == 0 else M[i][j]
    return M

def coin(M):
    '''
    Ajoute les coins à la matrice
    '''
    M[0][0],M[0][1],M[1][0] = 1 if randint(0, 10) % 2 == 0 else M[0][0], 1 if randint(0, 10) % 2 == 0 else M[0][1], 1 if randint(0, 10) % 2 == 0 else M[1][0]
    M[0][7],M[0][6],M[1][7] = 1 if randint(0, 10) % 2 == 0 else M[0][7], 1 if randint(0, 10) % 2 == 0 else M[0][6], 1 if randint(0, 10) % 2 == 0 else M[1][7]
    M[7][0],M[7][1],M[6][0] = 1 if randint(0, 10) % 2 == 0 else M[7][0], 1 if randint(0, 10) % 2 == 0 else M[7][1], 1 if randint(0, 10) % 2 == 0 else M[6][0]
    M[7][7],M[7][6],M[6][7] = 1 if randint(0, 10) % 2 == 0 else M[7][7], 1 if randint(0, 10) % 2 == 0 else M[7][6], 1 if randint(0, 10) % 2 == 0 else M[6][7]
    return M

def diagonal_1(M):
    '''
    Ajoute une diagonale à la matrice
    '''
    i = 0
    j = 0
    while(i < 8):
        if i == 0:
            M[i][i],M[i][1] = 1 if randint(0, 10) % 2 == 0 else M[i][i], 1 if randint(0, 10) % 2 == 0 else M[i][i]
        elif i == 7:
            M[i][i],M[i][6] = 1 if randint(0, 10) % 2 == 0 else M[i][i], 1 if randint(0, 10) % 2 == 0 else M[i][i]
        else:
            M[i][j],M[i][j+1],M[i][j-1] = 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j]
        i += 1
        j += 1
    return M

def diagonal_2(M):
    '''
    Ajoute une diagonale à la matrice
    '''
    i = 0
    j = 7
    while(i < 8):
        if i == 0:
            M[i][j],M[i][6] = 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j]
        elif i == 7:
            M[i][j],M[i][1] = 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j]
        else:
            M[i][j],M[i][j-1],M[i][j+1] = 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j], 1 if randint(0, 10) % 2 == 0 else M[i][j]
        i += 1
        j -= 1
    return M

# Crée 100 matrices pour chaque type de patern
for i in range(100):
    # Crée une matrice avec une ligne verticale
    M = create_blank_matrix()
    M = ligne_verticale(M)
    np.savetxt(f'vertical_line_{i}.csv', M, delimiter=',')

    # Crée une matrice avec une ligne horizontale
    M = create_blank_matrix()
    M = ligne_horizontale(M)
    np.savetxt(f'horizontal_line_{i}.csv', M, delimiter=',')

    # Crée une matrice avec un centre
    M = create_blank_matrix()
    M = centre(M)
    np.savetxt(f'center_{i}.csv', M, delimiter=',')

    # Crée une matrice avec une bordure
    M = create_blank_matrix()
    M = coin(M)
    np.savetxt(f'coins_{i}.csv', M, delimiter=',')

    # Crée une matrice avec une diagonal 1
    M = create_blank_matrix()
    M = diagonal_1(M)
    np.savetxt(f'diagonal_1_{i}.csv', M, delimiter=',')

    # Crée une matrice avec une diagonal 2
    M = create_blank_matrix()
    M = diagonal_2(M)
    np.savetxt(f'diagonal_2_{i}.csv', M, delimiter=',')