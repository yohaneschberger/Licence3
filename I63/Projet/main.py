import time
import numpy as np
from scene import Scene
from camera import Camera
from sphere import Sphere
from plan import Plan
from parallelipipede import Parallelipipede
from triangle import Triangle


t0 = time.time()

camera = Camera([500, 500], [0, 0, 0], [0, 0, 1], [0, 1, 0], 1)
scene = Scene(camera, [], [], 0.1, np.zeros((500, 500, 3)))
scene.add_objet(Sphere([0, 0, 1], 0.5, [1, 0, 0], 0.5))
scene.add_objet(Sphere([1, 1, 1], 0.5, [0, 1, 0], 0.5))
scene.add_objet(Plan([0, 0, 0], [0, 0, 1], [0, 0, 1], 0.5))
scene.add_objet(Parallelipipede([0, 0, 0], 1, 1, 1, [0, 1, 1], 0.5))
scene.add_objet(Triangle([0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 1, 1], 0.5))
scene.construire_image()

print('Temps de rendu :', time.time() - t0, 's')