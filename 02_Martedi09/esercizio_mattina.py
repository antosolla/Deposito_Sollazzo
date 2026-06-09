print("1. Numero pari o dispari \n 2. Conto alla rovescia \n 3. Quadrato di un numero \n 4. Massimo, numero elementi e check sulla lunghezza \n Altro. Esci")

scelta = int(input("Inserisci la tua scelta: "))
lista = []
match scelta:
    case 1:
        print("Inserisci un numero")
        numero = int(input())
        if numero % 2 == 0: #operatore modulo, se resto uguale a 0, allora è pari
            print("Pari")
        else:
            print("Dispari") #altrimenti dispari
    case 2:
        flag = True
        while flag:
            print("Inserisci un numero: ")
            n = int(input()) #faccio il cast a intero
            for i in range(n, 0, -1): #parto da n, arrivo a 0, e faccio step di -1
                print(i)
            print("Vuoi continuare? (si/no)")
            selezione = input()
            if selezione == "no":   #spunto il flag in questo caso e posso uscire dal ciclo
                flag = False
                
    case 3:
        print("Quanti valori vuoi inserire: ")
        n = int(input())
        for i in range(0,n): #vado da 0 fino a n-1 perchè comrpendo lo zero
            print("Inserisci un valore: ")
            numero = int(input())
            lista.append(n ** 2) #
        print(lista)
        
    case 4:
        print("Quanti valori vuoi inserire: ")
        n = int(input())
        for i in range(0,n): #vado da 0 fino a n-1 perchè comrpendo lo zero
            print("Inserisci un valore: ")
            numero = int(input())
            lista.append(n)
        
        max_numero = lista[0]
        for i in lista:
            if lista[i] > max_numero:   #sistema per trovare il max, passo tutti gli elementi al setaccio, ogni volta che è maggiore del max trovato, lo sostituscie
                max_numero = lista[i]
        
        counter = 0
        while counter <= len(lista):    #so a prescinrere la grandezza della lista, percio credo un contatore che si incrementa ad ogni iterata
            counter = counter + 1
            lista.
        if counter == 0:
            print("Lista vuota")
        else:
            print("Lista non vuota ed il massimo è" + max_numero)
        
    case _:
        print("Uscita")
    
    
