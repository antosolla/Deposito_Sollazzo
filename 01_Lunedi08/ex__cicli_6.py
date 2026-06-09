controllore = True
while controllore:
    n = int(input("Countdown a partire da?"))

    for i in range(0, n, 1):    #non riuscivo a imposare lo step a -1, cosi ho pensato di creare una operazione che incrementasse la quantita da sottrare
        i = 1   #ovviamente parte da 1
        print(n)
        n = n - i
        i = i + 1
    
    print("Vuoi smettere?")
    selezione = input()
    if selezione == "si":   #esco dal ciclo una volta che il controllore diventa falso
           controllore = False