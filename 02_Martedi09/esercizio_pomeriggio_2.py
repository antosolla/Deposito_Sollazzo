def calcola_fibonacci(n):
    a = 0
    b = 1
    somma = 0
    lista_fibonacci = []
    for i in range(n):
        somma += a
        lista_fibonacci.append(a)
        a = b
        b = a + b

    return lista_fibonacci

print("Inserisci un numero n:")
n = int(input())
lista_fibonacci = calcola_fibonacci(n)
