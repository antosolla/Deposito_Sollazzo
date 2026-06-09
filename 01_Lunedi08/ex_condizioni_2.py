rubrica = ["Giacomo", "Antonio", "Roberto", "Salvo", "Luigi"] #creo una piccola rubrica
print("1 - Inserisci nome in rubrica \n 2- Modifica nome \n 3- Rimuovi dalla rubrica") #creo un menu di scelta
selezione = input();

if selezione >= 1 and selezione <=3:  #inserisco un controllo preventivo, in maniera tale da restringere il dominio di input
    if selezione == 1:
        nome = input("Qual è il nome da inserire")
        rubrica.insert(nome)    #operazione di inserimento in rubrica
        print("Nome inserito con successo")
    elif selezione == 2:
        vecchio_nome = input("Qual è il nome da modificare?")
        rubrica.remove(vecchio_nome) #operazione di rimozione in rubrica
        nuovo_nome = input("Qual è il nome da inserire")
        rubrica.insert(nuovo_nome) #operazione di inserimento in rubrica
    elif selezione == 3:
        nome = input("Qual è il nome da eliminare?")
        rubrica.remove(nome)    #operazione di inserimento in rubrica
else:
    print("Errore nella selezione") #indico che è stato inserito un valore non compreso tra 1 e 3



    
    
