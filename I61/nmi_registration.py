import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im = Image.open('lena.jpeg')
Imarray = np.asarray(Im)

plt.figure()
plt.imshow(Imarray, cmap='gray')

# Calculer et afficher la densité de probabilité de l'image
xe = np.asarray(range(np.amax(Imarray[:])+2))
H1, xe = np.histogram(Imarray.reshape(-1), bins=xe)
P1 = H1/Imarray.size
plt.figure()
plt.plot(P1)

# Calculer et afficher l'entropie de l'image

def entropie(PX):
    res = 0
    for x in PX:
        if x != 0:
            res -= x * np.log2(x)
    return res

res = entropie(P1)
print("Entropie de l'image : ", res)

# Densité de probabilité jointe lena et lena4 et Affichage de la densité de probabilité jointe

Im4 = np.repeat(np.repeat(Imarray[::4,::4], 4, axis=0), 4, axis=1)
xe = np.asarray(range(np.amax(Im4[:])+2))
H2, xe = np.histogram(Im4.reshape(-1), bins=xe)
P2 = H2/Im4.size
plt.figure()
plt.plot(P2)

# Entropie jointe lena et lena4 et Affichage de l'entropie conjointe

def conjointe(PXY):
    return entropie(PXY.flatten())

Z = np.zeros((256,256))
for i in range(Imarray.shape[0]):
    for j in range(Imarray.shape[1]):
        Z[Imarray[i,j],Im4[i,j]] += 1
Z /= Imarray.size
plt.figure()
plt.imshow(Z, cmap='gray')


# NMI entre lena et lena4 et Affichage de l'information mutuelle normalisée
def NMI(I1, I2):
    # Calculer et afficher la densité de probabilité de l'image I1
    xe1 = np.asarray(range(np.amax(I1[:])+2))
    H1, xe1 = np.histogram(I1.reshape(-1), bins=xe1)
    P1 = H1/I1.size
    
    # Calculer et afficher la densité de probabilité de l'image I2
    xe2 = np.asarray(range(np.amax(I2[:])+2))
    H2, xe2 = np.histogram(I2.reshape(-1), bins=xe2)
    P2 = H2/I2.size
    
    # Calculer et afficher la densité de probabilité jointe des images I1 et I2
    Z = np.zeros((256,256))
    for i in range(I1.shape[0]):
        for j in range(I1.shape[1]):
            Z[I1[i,j],I2[i,j]] += 1
    Z /= I1.size
    
    # Calculer l'entropie de l'image I1
    H_I1 = entropie(P1)
    
    # Calculer l'entropie de l'image I2
    H_I2 = entropie(P2)
    
    # Calculer l'entropie conjointe des images I1 et I2
    H_I1_I2 = conjointe(Z)
    
    # Calculer l'information mutuelle entre les images I1 et I2
    MI = H_I1 + H_I2 - H_I1_I2
    
    # Calculer la normalisation de l'information mutuelle
    NMI = MI / np.sqrt(H_I1 * H_I2)
    
    return NMI

# Utilisation de la fonction NMI avec les images Imarray et Im4
nmi = NMI(Imarray, Im4)
print("Information mutuelle normalisée : ", nmi)

plt.show()

