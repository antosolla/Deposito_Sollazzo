flag = True #il flag è su True per entrare dentro il ciclo
numeri = [] #definisco la struttra
while flag:
    numero = int(input("Inserisci un numero"))
    
    if (len(numeri) == 4):  #dunque, siamo gia a quota 5? se si, possiamo uscire dal ciclo, altrimenti restiamo dentro
        flag = False    
    
    if numero % 2 != 0: #verifica numero primo, uso l'opeatore resto
        print("Il numero è primo")
        numeri.append(numero)   #visto che è primo, lo inseirco nella struttra dati
    else:
        print("Il numero non è primo")

print(numeri)
