#blocco if

numero = 10

if (numero == 10): #le condizione lavorano su TRUE, ovvero, la condizione al suo interno deve essere vero per eseguire il blocco di istruzioni
    print("vero")

if numero != 10: #ad esempio, la domanda qui è "è vero che è non uguale?"
        print("falso")
        
#blocco if  else

numero = 10
if numero > 0: 
    print("Il numero è positivo")
else:
    print("Blocco Else")
    
    
#blocco if elif else
numero = 100
if numero > 0: 
    print("Il numero è positivo")
    if numero == 100:
      print("wow è 100")
elif numero < 0: #qui posso essere piu inclusivo, ad esempio
    print("Il numero è negativo")
    
else:
    print("Il numero è zero")
    
#lo switch case
comando = input("Inserisci un comando: ")
match comando: #se comando sarà corrispondente ad uno dei seguenti casi, allorà verrà eseguito il codice associato
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _: #è il valore default, corrisponde all'else per l'if, in questo caso, tutti i valori non elecati nei casi sopra
        print("Comando non riconosciuto.")