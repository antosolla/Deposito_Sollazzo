flag = True
numeri = []
while flag:
    numero = int(input("Inserisci un numero"))
    
    if (len(numeri) == 4):
        flag = False
    
    if numero % 2 != 0:
        print("Il numero è primo")
        numeri.append(numero)
    else:
        print("Il numero non è primo")

print(numeri)
