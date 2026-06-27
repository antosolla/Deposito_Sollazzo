import numpy as np

def dimensioni():
    m = int(input("Inserisci numero di righe della matrice: "))
    n = int(input("Inserisci numero di colonne della matrice: "))
    return m, n

def crea_matrice(m, n):
    matrice = np.random.randint(1, 10, size=(m, n))
    save_matrice(matrice, filename)
    return matrice

def extract_centrale(matrice):
    if matrice is not None:
        m, n = matrice.shape
        if m >= 3 and n >= 3:
            centrale = matrice[1:m-1, 1:n-1]
            print(centrale)
            operazione = "Estrazione centrale"
            save_matrice(matrice, filename, operazione)
        else:
            centrale = None
            print("Non è possibile estrarre la matrice centrale")
        return centrale
    else:
        print("Nessuna matrice inserita.")

def transpose_matrice(matrice):
    if matrice is not None:
        operazione = "Trasposta"
        save_matrice(matrice.T, filename, operazione)
        print(matrice.T)
        return matrice.T
    else:
        print("Nessuna matrice inserita.")

def sum_and_print(matrice):
    if matrice is not None:
        somma = np.sum(matrice)
        operazione = "Somma"
        print("La somma di tutti gli elementi della matrice è:", somma)
        save_scalare(somma, filename, operazione)
        return somma
    else:
        print("Nessuna matrice inserita.")

def moltiplicazione_valori(matrice):
    if matrice is not None:
        m, n = matrice.shape[0], matrice.shape[1]
        matrice_2= crea_matrice(m,n)
        print("Matrice 2:\n", matrice_2)
        prodotto_el_wise = matrice * matrice_2
        operazione = "Moltiplicazione el-wise"
        print("Totale moltiplicazione:\n", prodotto_el_wise)
        save_matrice(prodotto_el_wise, filename, operazione)
        return prodotto_el_wise
    else:
        print("Nessuna matrice inserita.")
    
def media_valori(matrice):
    if matrice is not None:
        media = np.mean(matrice)
        operazione = "Media"
        print("Media:", media)
        save_scalare(media, filename, operazione)
        return media
    else:
        print("Nessuna matrice inserita")

def save_matrice(matrice, filename, operazione):
    with open(filename, 'a') as f:
        f.write(operazione + '\n')
        for riga in matrice:
            f.write(' '.join(map(str, riga)) + '\n')

def save_scalare(scalare, filename, operazione):
    with open(filename, 'a') as f:
        f.write(operazione + '\n')
        f.write(str(scalare) + '\n')
        
print("MENU")
print("1 - Crea una nuova matrice")
print("2 - Estrai la sottomatrice centrale")
print("3 - Trasponi la matrice")
print("4 - Somma gli elementi della matrice")
print("5 - Moltiplicazione element-wise")
print("6 - Media degli elementi della matrice")
print("999 - Esci")

matrice = None
filename = "risultati_new.txt"

while True:
    scelta = input("Cosa vuoi fare? ")
    match scelta:
        case "1":
            m, n = dimensioni()
            matrice = crea_matrice(m, n)
            print(matrice)
        case "2":
            extract_centrale(matrice)
        case "3":
            transpose_matrice(matrice)
        case "4":
            sum_and_print(matrice)
        case "5":
            moltiplicazione_valori(matrice)
        case "6":
            media_valori(matrice)
        case "999":
            print("Programma terminato")
            break
        case _:
            print("Opzione non valida")