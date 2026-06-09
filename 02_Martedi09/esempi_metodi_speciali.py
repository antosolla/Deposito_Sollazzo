#generatori
def fibonacci(n):
    a, b = 0, 1

    while a < n:
        yield a #yield è come un return, ma la funzione non ha terminato la sua esecuzione, può essere ripresa da dove è stata interrotta
        a, b = b, a + b 

coll = [*fibonacci(100)] #crea un oggetto generatore
for numero in fibonacci(100):
    print(numero)
print(coll)

#decoratori
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")

saluta()
