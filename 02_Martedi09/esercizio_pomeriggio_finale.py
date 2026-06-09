def numero_casuale(n):
    import random
    return random.randint(1, n)
flag = False

def calcola_somma_n_pari():
    somma = 0
    for numero in lista:
        if numero % 2 == 0:
            somma += numero
    print("La somma dei numeri pari è:", somma)

def stampa_dispari(lista):
    for numero in lista:
        if numero % 2 != 0:
            print(f"Il numero {numero} è dispari.")

def crea_lista_primi(lista):
    #uso formula del polinomio n^2 + n + 41, con n massimo a 39
    for i in range(40): #39 incluso, quindi fino a 40
        lista_primi = [] #inizializzo la lista dei primi
        primo = i**2 + i + 41 #calcolo elemento primo con la formula del polinomio
        lista_primi.append(primo) #aggiungo il numero alla lista dei primi
    return lista_primi

def check_primo(numero, lista_primi):
    #funzione che verifica se un numero è primo, controllando la sua presenza nella lista calcolata tramite polinomio
    flag = False
    for primo in lista_primi:
        if numero == primo:
            flag = True
    return flag

def somma_numeri(lista):
    somma = 0
    for numero in lista:
        somma += numero
    return somma

numero = 0 #inizializzo la variabile numero a 0
lista = []  #inizializzo la lista dei numeri
lista_primi = [] #inizializzo la lista dei numeri primi

while True:
    selezione = int(input("Scegli un'opzione:\n1. Inserire un numero positivo\n2. Generare una lista di numeri casuali\n3. Calcolare la somma dei numeri pari\n4. Stampare i numeri dispari\n5. Verificare se un numero è primo\n6. Stampare i numeri primi nella lista\n7. Calcolare la somma dei numeri e verificare se è primo\n"))
    match selezione:
        case 1: 
            while flag!= False:
                print("Inserisci un numero positivo:")
                numero = int(input())
            if numero > 0:
                flag = True
            if numero < 40: #creo la lista dei numeri primi gia da ora, in maniera tale da averla gia pronta per dopo
                lista_primi = crea_lista_primi(lista)
        case 2:
            lista = []
            for i in range(numero): #richiamo la funzione numero volte
                lista.append(numero_casuale(numero))

        case 3:
            calcola_somma_n_pari()

        case 4:
            stampa_dispari(lista)

        case 5:
            check_primo = check_primo(numero, lista_primi)
            if check_primo:
                print("Il numero è primo.")
            else:
                print("Il numero non è primo.")
    
        case 6:
            for i in lista:
                if check_primo(i, lista_primi):
                    print(f"Il numero {i} è primo.")
    
        case 7:
            somma_numeri = somma_numeri(lista)
            if check_primo(somma_numeri, lista_primi):
                print(f"La somma dei numeri è {somma_numeri} ed è primo.")
        case _:
            print("Opzione non valida")
            break   #interrompo il ciclo