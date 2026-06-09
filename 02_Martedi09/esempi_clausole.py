#pass
for i in range(5):
    if i == 3:
        pass
print(i)  

#break
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)
    
#continue
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        continue
    print(numero)

#splat
numeri = [*range(1, 11)]    #le quadre servono per la lista, senza avrebbe creato tupla (che si crea anche con {}), () per gli insiemi 
print(numeri)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]