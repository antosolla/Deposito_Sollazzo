import numpy as np

def crea_matrice():
    m= int(input("Inserisci numero di righe della matrice: "))
    n = int(input("Inserisci numero di colonne della matrice: "))
    matrice = np.random.randint(1, 10, size=(m, n))
    return matrice

def extract_centrale(matrice):
    m, n = matrice.shape
    if m >= 3 and n >= 3:
        centrale = matrice[1:m-1, 1:n-1]
        print(centrale)
    else:
        centrale = None
    return centrale

matrice = crea_matrice()
print(extract_centrale(matrice))
