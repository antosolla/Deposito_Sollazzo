#EXTRA: decoratora nella funzione di login che verifica l'effettiva esistenza del cliente prima di continuare con la procedura di login

import modulo_Cliente
import modulo_Articolo
import modulo_Amministratore

inventario : list[modulo_Articolo.Articolo] = []    #creo una lista di articoli, per il momento vuota
clienti: list[modulo_Cliente.Cliente] = []  #idem per i clienti
admins: list[modulo_Amministratore.Amministratore] = []
ordini = []


def prodotti_disponibili():
    for articolo in inventario:
        if articolo.quantita > 0:
            yield articolo          #generatore di prodotti disponibili


def procedura_acquisto(utente: modulo_Cliente.Cliente):
    
    articoli_disp = prodotti_disponibili()
    
    print("Quale prodotto vuoi acquistare?")
    nome_articolo = input()
    print("In che quantita?")
    quantita_articolo = input()
    
    for articolo in articoli_disp:
        if nome_articolo == articolo.nome:  #verifico il nome
            if quantita_articolo > articolo.quantita:   #verifico quantita
                articolo.quantita = articolo.quantita - quantita_articolo
            else:
                importo = articolo.prezzo * quantita_articolo
            
            #verifica del credito
            if utente.wallet < importo:
                print("Credito insufficiente")
                break
            else:
                articolo.quantita = articolo.quantita - quantita_articolo
                utente.wallet -= importo
                print("Acquisto effettuato!")
                
                #vado a definire una struttura dati che contenga tutte le informazioni utili rispetto alla transazione
                ordine = {
                "id_cliente" : utente.id_cliente,
                "mail" : utente.email,
                "articolo": articolo.nome_articolo,
                "importo": importo
                }
                
                ordini.append(ordine)  #lista di dizionari, o lista di record per mantenere tutti gli ordini
                break
            
                
def crea_utente():
    
    print("Inserisci nome e cognome")
    nome_cognome = input()
    
    print("Inserisci indirizzo mail")
    email = input()
    
    print("Inserisci password")
    password = input()
    
    utente = modulo_Cliente.Cliente(nome_cognome, email, password)
    flag_gia_esistente = False
    
    for cliente in clienti: #grazie a questo metodo evito di avere la stessa mail inserita piu volte
        if email == cliente.email:
            break
    if not flag_gia_esistente:  #grazie al flag riesco a capire se è gia presente
            clienti.append(utente)
            print("Cliente aggiunto con successo")

            
def crea_admin():
    
    print("Inserisci nome e cognome")
    nome_cognome = input()
    
    print("Inserisci indirizzo mail")
    email = input()
    
    print("Inserisci password")
    password = input()
    
    admin = modulo_Amministratore.Amministratore(nome_cognome, email, password) #creo un oggetto admin da "appendere" alla lista degli admin
    flag_gia_esistente = False
    
    for elemento in admins: #grazie a questo metodo evito di avere la stessa mail inserita piu volte
        if email == elemento.email:
            flag_gia_esistente = True
            print("Amministratore gia presente")
            break
    if not flag_gia_esistente:  #idem qui, #grazie al flag riesco a capire se è gia presente
            admins.append(admin)
            print("Amministratore aggiunto con successo")
        

#grazie a questo decoratore posso controllare preventivamente che l'utente esista davvero
def check_utenti(func):
    def wrapper():
        print("Inserisci indirizzo email: ")
        email = input()
        flag_trovato = False
        for utente in clienti:
            if email == utente.email:
                func(email) #eseguo la funzione solo SE la mail è presente
                break
        if not flag_trovato:
            print("Utente non trovato")
        return wrapper

@check_utenti
def login(email):
    
    print("Inserisci password: ")
    password = input()
    for utente in clienti:
        if email == utente.email and password == utente.password:   #se entrambi i campi sono giusti, si procede col login
            return utente
        elif password != utente.password:
            print("Password non corretta")       
            
        

while True:
    
    #menu iniziale
    print("Vuoi accedere come: ")
    print("1. Cliente")
    print("2. Amministratore")
    selettore = int(input())
    
    match selettore:
        case 1:
            
            #fase dedicata al cliente
            print("1. Accedi")
            print("2. Registrati")
            selettore = int(input())
            
            match selettore:
                case 1:
                    utente = login()
                    #Accedi
                    print("1. Visualizza articoli disponibili")
                    print("2. Acquista un prodotto")
                    selettore = int(input())
                    match selettore:
                        case 1:
                            articoli_disp = prodotti_disponibili()
                            print("Lista articoli disponibili:")
                            for articolo in articoli_disp:
                                print(articolo.nome)
                        case 2:
                            procedura_acquisto(utente)  #la lista degli articoli disponibili è inclusa nella logica della funzione, è inutile passarla per paramentro
                            
                case 2:
                    #Registrazione
                    if (modulo_Amministratore.Amministratore.conta_admin <= 0):
                        print("Impossibile creare utente. Non sono presenti admin") #in questo modo rispetto il requisito che mi vincola a creare utente se è almeno presente un admin
                    else:
                        crea_utente() 
                case _:
                    print("Scelta non valida")
        case 2:
            #fase dedicata all'admin
            print("1. Accedi")
            print("2. Registrati")
            selettore = int(input())

            match selettore:
                case 1:
                    #devo creare procedura di accesso
                    print("1. Stampa report vendite")
                    for i in ordini:
                        print(f"Id del cliente: {i["id_cliente"]}, mail del cliente: {i["mail"]}", )
                        #non ho tempo di finire, ma il senso è quello di stampare tutta la lista degli ordini accedendo ai campi
                    print("2. Registrati")
                    
                case 2:
                   crea_admin() 
                case _:
                    print("Scelta non idonea")