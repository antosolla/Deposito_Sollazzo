rubrica = ["Giacomo", "Antonio", "Roberto", "Salvo", "Luigi"] #creo una piccola rubrica
print("1 - Inserisci nome in rubrica \n 2- Modifica nome \n 3- Rimuovi dalla rubrica") #creo un menu di scelta
selezione = input();

if selezione >= 1 and selezione <=3:
    if selezione == 1:
        nome = input("Qual è il nome da inserire")
        rubrica.insert(nome)
        print("Nome inserito con successo")
    elif selezione == 2:
        vecchio_nome = input("Qual è il nome da modificare?")
        rubrica.remove(vecchio_nome)
        nuovo_nome = input("Qual è il nome da inserire")
        rubrica.insert(nuovo_nome)
    elif selezione == 3:
        nome = input("Qual è il nome da eliminare?")
        rubrica.remove(nome)
else:
    print("Errore nella selezione") #indico che è stato inserito un valore non compreso tra 1 e 3



    
    
