import numpy as np
import csv
import os
from PIL import Image

import matplotlib.pyplot as plt

############################################

# dictionnaire des fichiers CSV par classe
images_by_class = {
    'class1': [f'horizontal_line_{i}.csv' for i in range(100)],
    'class2': [f'vertical_line_{i}.csv' for i in range(100)],
    'class3': [f'diagonal_1_{i}.csv' for i in range(100)],
    'class4': [f'diagonal_2_{i}.csv' for i in range(100)],
    'class5': [f'center_{i}.csv' for i in range(100)],
    'class6': [f'coins_{i}.csv' for i in range(100)]
}

EPSILON = 1e-6

############################################

def load_csv(file_path):
    with open(file_path, 'r') as f:
        data = csv.reader(f)
        data = list(data)
        data = np.array(data, dtype=float)
    return data

# Ajoute du bruit à une image en inversant aléatoirement certains pixels 0 et 1
def bruitage(image, db):
    '''
    Ajoute du bruit à une image en inversant aléatoirement certains pixels 0 et 1
    '''
    # Calcule le nombre de pixels à inverser
    nb_pixels = int(db / 100 * image.size)
    
    # Inverse aléatoirement les pixels
    pixels = np.random.choice(image.size, nb_pixels, replace=False)
    image = image.copy()
    image.ravel()[pixels] = 1 - image.ravel()[pixels]
    
    return image

def calculate_probabilities(image):
    # Calcule la probabilité de chaque valeur
    unique, counts = np.unique(image, return_counts=True)
    probabilities = counts / np.sum(counts)

    return probabilities

def shannon_entropy_image(image):
    # Calcule la densité de probabilité
    probabilities = calculate_probabilities(image)

    # Calcule l'entropie de Shannon
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))

    return shannon_entropy

# Calcul de la divergence KL entre deux fichiers CSV
def kl_divergence(file_path1, file_path2):
    # Charge les fichiers CSV
    data1 = load_csv(file_path1)
    data2 = load_csv(file_path2)
    
    # Calcule la probabilité de chaque valeur
    unique1, counts1 = np.unique(data1, return_counts=True)
    probabilities1 = counts1 / np.sum(counts1)
    
    unique2, counts2 = np.unique(data2, return_counts=True)
    probabilities2 = counts2 / np.sum(counts2)
    
    # Calcule la divergence KL
    kl_divergence = np.sum(probabilities1 * np.log2(probabilities1 / probabilities2))
    
    return kl_divergence

# Calcule la divKL moyenne pour chaque pixel
divKL_avg = []
for pixel in range(64):
    divKL_sum = 0
    for class1 in images_by_class:
        for class2 in images_by_class:
            divKL_sum += kl_divergence(images_by_class[class1][pixel], images_by_class[class2][pixel])
    divKL_avg.append(divKL_sum / 36)

# Trie les pixels dans l'ordre décroissant de DIV(j)
sorted_pixels = sorted(range(64), key=lambda x: divKL_avg[x], reverse=True)

# Garde seulement les 32 premiers pixels
top_pixels = sorted_pixels[:32]

# Convertit les indices des pixels en coordonnées 2D (i, j)
top_pixels_2d = [(pixel // 8, pixel % 8) for pixel in top_pixels]

# Crée une matrice de 8x8 pour afficher les pixels les plus importants
top_pixels_matrix = np.zeros((8, 8))
for i, j in top_pixels_2d:
    top_pixels_matrix[i, j] = 1

# Affiche les pixels les plus importants
plt.imshow(top_pixels_matrix, cmap='gray')
plt.show()

# Met à jour les fonctions pour utiliser seulement les pixels les plus importants
def shannon_entropy_image_by_class_top_pixels(image_by_class):
    # Charge les fichiers CSV
    data = [load_csv(file_path) for file_path in image_by_class]

    # Garde seulement les pixels les plus importants
    data = np.array(data)[[index for index in top_pixels_2d]]

    # Calcule la probabilité de chaque valeur
    unique, counts = np.unique(data, return_counts=True)
    probabilities = counts / np.sum(counts)

    # Calcule l'entropie de Shannon
    shannon_entropy = -np.sum(probabilities * np.log2(probabilities))

    return shannon_entropy

def kl_divergence_image_by_class_top_pixels(image_by_class1, image_by_class2):
    # Charge les fichiers CSV
    data1 = [load_csv(file_path) for file_path in image_by_class1]
    data2 = [load_csv(file_path) for file_path in image_by_class2]
        
    # Garde seulement les pixels les plus importants
    data1 = np.array(data1)[[index for index in top_pixels_2d]]
    data2 = np.array(data2)[[index for index in top_pixels_2d]]
        
    # Calcule la probabilité de chaque valeur
    unique1, counts1 = np.unique(data1, return_counts=True)
    probabilities1 = counts1 / np.sum(counts1)
        
    unique2, counts2 = np.unique(data2, return_counts=True)
    probabilities2 = counts2 / np.sum(counts2)
        
    # Calcule la divergence KL
    kl_divergence = np.sum(probabilities1 * np.log2(probabilities1 / probabilities2))
        
    return kl_divergence

def barycenter_image_by_class_list_top_pixels(image_by_class_list):
    '''
    Calcule le barycentre des images de chaque classe
    '''
    # Charge les fichiers CSV
    data_list = [[load_csv(file_path) for file_path in image_by_class] for image_by_class in image_by_class_list]
        
    # Garde seulement les pixels les plus importants
    data_list = np.array(data_list)[:, [index for index in top_pixels_2d]]
        
    # Calcule le barycentre
    barycenter = np.mean(data_list, axis=0)
        
    return barycenter

def probability_density_image_by_class_top_pixels(image_by_class):
    '''
    Calcule la densité de probabilité des pixels les plus importants pour une classe
    '''
    # Charge les fichiers CSV
    data = [load_csv(file_path) for file_path in image_by_class]
        
    # Garde seulement les pixels les plus importants
    data = np.array(data)[[index for index in top_pixels_2d]]
        
    # Calcule la densité de probabilité
    unique, counts = np.unique(data, return_counts=True)
    probabilities = counts / np.sum(counts)
        
    return probabilities

def probability_density_image_by_class_list_top_pixels(image_by_class_list):
    '''
    Calcule la densité de probabilité des pixels les plus importants pour une liste d'images de classes différentes
    '''
    # Charge les fichiers CSV
    data_list = [[load_csv(file_path) for file_path in image_by_class] for image_by_class in image_by_class_list]
        
    # Garde seulement les pixels les plus importants
    data_list = np.array(data_list)[:, [index for index in top_pixels_2d]]
        
    # Calcule la densité de probabilité, unique est un tableau de valeurs uniques, counts est un tableau de fréquences de ces valeurs
    unique, counts = np.unique(data_list, return_counts=True)
    probabilities = counts / np.sum(counts)
        
    return probabilities

def create_reference_images(images_by_class):
    '''
    Crée une image de référence pour chaque classe
    '''
    reference_images = {}

    for class_name, image_files in images_by_class.items():
        # Charge les images pour cette classe
        images = [load_csv(file) for file in image_files]

        # Calcule l'image moyenne pour cette classe
        average_image = np.mean(images, axis=0)

        # Stocke l'image moyenne comme image de référence pour cette classe
        reference_images[class_name] = average_image

    return reference_images

def calculate_accuracy(image, reference_image):
    '''
    Calcule la précision entre une image et une image de référence
    '''
    # Calcule la précision
    accuracy = np.mean(image == reference_image)

    # Convertit en pourcentage
    accuracy_percentage = accuracy * 100

    return accuracy_percentage

def calculate_score(image, reference_image):
    # Calcule le score
    score = np.sum(image == reference_image) / image.size

    return score

# Fonction qui affiche les courbes de toutes les classes en même temps sur le même graphe, axe x: db, axe y: accuracy
def plot_accuracy_vs_db(images_by_class):
    '''
    Affiche les courbes de précision en fonction du RSB
    '''
    fig, ax = plt.subplots(figsize=(10, 5))
    for class_name, image_files in images_by_class.items():
        image = load_csv(image_files[0])
        reference_image = create_reference_images(images_by_class)[class_name]
        db_values = np.arange(0, 101, 5)
        accuracies = []
        for db in db_values:
            noisy_image = bruitage(image, db)
            accuracy = calculate_accuracy(noisy_image, reference_image)
            accuracies.append(accuracy)
        ax.plot(db_values, accuracies, label=class_name)
    ax.set_xlabel('db')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Accuracy vs dB')
    ax.legend()
    plt.show()

# Fonction qui affiche toutes les courbes de scores pour le RSB de 0 à 100 dB
def plot_score_vs_db(images_by_class):
    fig, ax = plt.subplots(figsize=(10, 5))
    for class_name, image_files in images_by_class.items():
        image = load_csv(image_files[0])
        reference_image = create_reference_images(images_by_class)[class_name]
        db_values = np.arange(0, 101, 5)
        scores = []
        for db in db_values:
            noisy_image = bruitage(image, db)
            score = calculate_score(noisy_image, reference_image)
            scores.append(score)
        ax.plot(db_values, scores, label=class_name)
    ax.set_xlabel('dB')
    ax.set_ylabel('Score')
    ax.set_title('Score vs dB')
    ax.legend()
    plt.show()

    

############################################

def main():
    # Calcule l'entropie de Shannon d'un fichier CSV
    shannon_entropy_value = shannon_entropy_image_by_class_top_pixels(images_by_class['class1'])
    print(f"Entropie de Shannon: {shannon_entropy_value}")
        
    # Calcule la divergence KL entre deux fichiers CSV
    kl_divergence_value = kl_divergence_image_by_class_top_pixels(images_by_class['class1'], images_by_class['class2'])
    print(f"Divergence KL: {kl_divergence_value}")
        
    # Calcule le barycentre d'une image_by_class de fichiers CSV
    barycenter_value = barycenter_image_by_class_list_top_pixels([images_by_class['class1'], images_by_class['class2']])
    print(f"Barycentre: {barycenter_value}")
        
    # Calcule la densité de probabilité d'un fichier CSV
    probability_density_value = probability_density_image_by_class_top_pixels(images_by_class['class1'])
    print(f"Densité de probabilité: {probability_density_value}")

    # Calcule la densité de probabilité d'une image_by_class de fichiers CSV
    probability_density_value = probability_density_image_by_class_list_top_pixels([images_by_class['class1'], images_by_class['class2']])
    print(f"Densité de probabilité: {probability_density_value}")

    # Affiche les courbes de précision en fonction du RSB
    plot_accuracy_vs_db(images_by_class)

    # image de référence pour la classe 1
    reference_image = create_reference_images(images_by_class)['class1']

    # Affiche la référence
    plt.imshow(reference_image, cmap='gray')
    plt.show()
    

if __name__ == '__main__':
    main()
