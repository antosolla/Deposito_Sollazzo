controllore = True
while controllore:
    n = int(input("Countdown a partire da?"))

    for i in range(0, n, 1):
        i = 1
        print(n)
        n = n - i
        i = i + 1
    
    print("Vuoi smettere?")
    controllore = False