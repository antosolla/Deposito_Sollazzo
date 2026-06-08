#while
conteggio = 0
while conteggio < 5: #finche la condizione è vera, cicla ed esegue il blocco istruzioni
    print(conteggio)
    conteggio += 1 #incrementa di uno
    
controllore = True

while controllore: #controllore in questo momento è true, percio continuo ad eseguire
    print("Ciao")
    
    #esericizi
    
    scelta = input("vuoi continuare?")
    if scelta == "no":
        controllore = False
        
#ciclo for
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
    
#Range con Stop
for i in range(5): #in questo caso ho definito solo lo stop, è di default lo step uguale a 1 e la base da cui partire che è 0
    print(i)

#Range con Start e Stop, nota: lo stop è sempre N-1
for i in range(2, 8):
    print(i)
    
#Range con Start, Stop e Step
for i in range(1, 10, 2):
    print(i)

