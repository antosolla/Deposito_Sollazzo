
# le credenziali corrette sono Antonio Sollazzo 29

nome = input("Primo step, inserisci nome") #chiedo nome in input
if (nome == "Antonio"):
    cognome = input("Secondo step, inserisci cognome") #chiedo cognome in input
    if (cognome == "Sollazzo"):
        eta = int(input("Terzo ed ultimo step, inserisci eta"))
        if (eta == 29):
            print("Hai superato tutti gli step. Sei autenticato.") # a questo if arrivo SOLTANTO SE prima con successo, son passato dai precendeti
else:
    print("Errore. Nome inserito non corretto") #esco subito fuori dal ciclo, il nome è errato
        
