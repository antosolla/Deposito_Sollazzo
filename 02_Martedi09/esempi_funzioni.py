def saluta(nome):
    print("Ciao,", nome)

def saluta(nome):
    print("Ciao,", nome)
    print("Benvenuto nel nostro programma!")

def somma(a, b):    #a e b sono placeholder
    risultato = a + b
    print("La somma è:", risultato)
    
saluta("Alice")   
somma(5, 3)       
# Output: Ciao, Alice
# Output: La somma è: 8

def quadrato(numero):
    return numero * numero  #qui ho un return, probabilmente usato per valorizzare cose

risultato = quadrato(4) #passo il valore 4
print(risultato)          
# Output: 16

