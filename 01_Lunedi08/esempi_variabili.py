#I primi esempi
""" nome = "Antonio"
eta = 29
print("Il mio nome è", nome, "e ho", eta, "anni") """

""" nome = input("Inserisci nome") #questa è funzione integrata
eta = int(input("Inserisci la tua eta")) #gli input sono SEMPRE stringhe, le casto perciò in int

print("Ciao, " + nome + "! Benvenuto in Python!")

spazio = " " #posso avere anche escamotage con spazio.
print(nome + spazio + eta)


 """
#Operazioni matematiche
""" print(1+5) #6 posso processare dei calcoli dentro una funzione intrinseca, l'OOP funziona
print(6-5) #differenza
print(6*1) #moltiplicazione
print(6 /1) #divisione
print(5**2) #potenza """

#I tipi in Python
""" 
Esempi di numeri in Python:
x  = 10 # Alcuni esempi di interi in Python
y = - 5 # Alcuni esempi di interi in Python

Esempi di numeri in virgola mobile in Python:
a  =  3.14 # Alcuni esempi di numeri in virgola mobile in Python
b = - 1.0 # Alcuni esempi di numeri in virgola mobile in Python

Esempi di stringhe in Python:

nome  = 'Alice' # Alcuni esempi di stringhe in Python
msg = "Ciao!"  # Alcuni esempi di stringhe in Python """

# Gli indici.

s = "Anto"
print(s[0]) #stampo la prima lettera

# Concatenare.
saluto  =  "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome #"Somma" di stringhe. Una sorta di append
print(messaggio) # Output: 'Ciao Alice'

#I metodi delle stringhe e le funzioni
s  =  "Ciao, mondo!"
print(len(s)) # Output: 12 la funzione non ha bisogno di richiami, il metodo si. NOTA: le parentisi identificano quasi sempre un metodo/funzione
print(s.upper()) # Output: 'CIAO, MONDO!'
print(s.split(',')) # Output: '[CIAO] , [MONDO!]' #come nel file CSV, ho un separatore, in questo caso la virgola
print(s.replace('mondo', 'universo')) # Output: 'Ciao, universo!' #replace serve a rimpiazzare una parola (all'interno di una stringa) con un'altra

#Booleani. Dentro il print non ho condizioni, ma confronti
x = 5
y = 10
print(x == y) # Output: False #operatore uguale
print(x != y) # Output: True #operatore NON uguale
print(x < y) # Output: True #opeatore minore di

#Operatori logici
x = 5
y = 10
z = 7
print(x < y and y > z) # Output: True #entrambe le "affermazioni" devono essere vere per avere in out TRUE
print(x < y or z > y) # Output: True #basta che una delle due "affermazioni" sia vera e restituisco true
print(not(x < y)) # Output: False

#Liste

#procedo col definire delle liste, alcune omo, l'ultima etero
numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]

#per accedere ad un elemento si usa sempre l'indice, come nelle stringhe
numeri = [1, 2, 3, 4, 5]
print(numeri[0])   
# Output: 1
print(numeri[2])   
# Output: 3

#esempi di metodi con le liste
numeri = [3, 1, 4, 2, 5]
print(len(numeri))   # Output: 5 #stampo la size della lista
numeri.append(6)     #aggiungo in fondo alla lista il valore 6
print(numeri)        # Output: [3, 1, 4, 2, 5, 6] #faccio una stampa totale
numeri.insert(2, 10)
print(numeri)        # Output: [3, 1, 10, 4, 2, 5, 6] #inserisco all'indice 2 il numero 10
numeri.remove(4)     #rimuovo l'elemento 4, non quarto!
print(numeri)        # Output: [3, 1, 10, 2, 5, 6]
numeri.sort()           #banalmente, ordino
print(numeri)        # Output: [1, 2, 3, 5, 6, 10]

