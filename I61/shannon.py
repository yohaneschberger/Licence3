import numpy as np

def entropie(PX):
    res = 0
    for x in PX:
        res -= x * np.log2(x)
    return res

def conjointe(PXY):
    return entropie(PXY.flatten())

def InfoMut(PXY):
    ePXY = conjointe(PXY)
    PX = np.sum(PXY,0)
    PY = np.sum(PXY,1)
    ePX = entropie(PX)
    ePY = entropie(PY)
    return ePY - ePXY + ePX

def entropie_croise(P,Q):
    return -np.sum(P * np.log2(Q))

def distance_entropie(PXY):
    return conjointe(PXY) - InfoMut(PXY)

X = np.array([0.3,0.7])
res = entropie(X)

Z = np.array([[0.25,0.25],[0.125,0.375]])
res2 = InfoMut(Z)

print("Entropie de Shannon : ", res)
print("Entropie Conjointe : ", conjointe(Z))
print("Information Mutuelle : ", res2)

