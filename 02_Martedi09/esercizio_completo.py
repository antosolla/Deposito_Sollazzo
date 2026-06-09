numero = 1  #inizializzo la variabile numero a un valore positivo per entrare nel ciclo
somma = 0 #inizializzo la variabile somma a 0


while numero > 0:
    print("Inserisci un numero intero positivo: ")
    numero = int(input())  #lo casto in int
    
    if numero > 0: #se il numero è positivo, allora eseguo il ciclo for
        for i in range(1, numero+1): #il range  arriva fino a n
            if i % 2 == 0: #se il numero è pari, stampo
                somma = somma + i
                
        #stampa dei numeri dispari
        for i in range(1, numero+1):
            if i % 2 != 0: #se il numero è dispari, stampo
                print(i)
        #uso formula del polinomio n^2 + n + 41, con n massimo a 39
        #creo una listi dei numeri primi, dopo verifico presenza dentro la lista
        for i in range(40): #39 incluso, quindi fino a 40
            lista_primi = [] #inizializzo la lista dei primi
            primo = i**2 + i + 41 #calcolo elemento primo
            lista_primi.append(primo) #aggiungo il numero alla lista dei primi
        if numero in lista_primi: #se il numero è nella lista dei primi, allora è primo
            print("Il numero è primo.")