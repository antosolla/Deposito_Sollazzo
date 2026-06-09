#genera numero causale tra 1 e 100 inclusi
import random

flag_indovinato = False #setto il flag indovinato a false, cosi posso entrare nel ciclo

def genera_causale():
    #funzione che genera un numero causale intero tra 1 e 100
    causale = random.randint(1, 100)
    return causale

def confronta(numero: int, n_causale: int):
    #funzione che confronta il numero inserito con il numero causale
    if numero == n_causale:
        print("Hai indovinato!")
        return True
    elif numero < n_causale:
        print("Il numero causale è più grande.")
        return False
    else:
        print("Il numero causale è più piccolo.")
        return False

n_causale = genera_causale() #assegno alla variabile il valore random restuito da genera_causale
while not flag_indovinato:
    #itero finche non viene indovinato, faccio cio tramite il flag indovinato
    print("Indovina il numero causale tra 1 e 100")
    numero=int(input())
    flag_indovinato = confronta(numero, n_causale)