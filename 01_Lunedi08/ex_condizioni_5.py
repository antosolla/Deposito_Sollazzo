valore1 = input("Inserisci il primo valore")
valore2 = input("Inserisci il secondo valore")
#prendo in input i due valori

print("Che operazione matematica vuoi eseguire? 1. Somma 2. Differnza 3. Prodotto 4. Divisione")
selezione = input();
#stampo una lista di valori selezionabili e faccio scegliere all'utente

match selezione:
    case "1":
        somma = valore1 + valore2 #eseguo somma dei valori
        print(somma)
    case "2":
        differenza = valore1 - valore2 #eseguo diffenza dei valori
        print(differenza)
    case "3":
        prodotto = valore1 * valore2 #eseguo prodotto dei valori
        print(prodotto)
    case "4":
        if valore2 == 0:
            print("impossibile dividere per zero") #qui controllo che il DEN sia diverso da zero per poter effettivamente procedere
        else:
            quoziente = valore1 / valore2 #eseguo la divisione dei valori
            print(quoziente)
    case _:
        print("Selezione del comando non corretta")