import modulo_Cliente
import modulo_Articolo

inventario : list[modulo_Articolo.Articolo] = []    #creo una lista di articoli, per il momento vuota
clienti: list[modulo_Cliente.Cliente] = []

def prodotti_disponibili():
    for articolo in inventario:
        if articolo.quantita > 0:
            yield articolo          #generatore di prodotti disponibili

def procedura_acquisto():
    
    articoli_disp = prodotti_disponibili()
    
    print("Quale prodotto vuoi acquistare?")
    nome_articolo = input()
    print("In che quantita?")
    quantita_articolo = input()
    
    for articolo in articoli_disp:
        if nome_articolo == articolo.nome:
            if quantita_articolo > articolo.quantita:
                articolo.quantita = articolo.quantita - quantita_articolo
    
    
    
            
def crea_utente():
    
    print("Inserisci nome e cognome")
    nome_cognome = input()
    
    print("Inserisci indirizzo mail")
    email = input()
    
    utente = clienti(nome_cognome, email)
    flag_gia_esistente = False
    
    for cliente in clienti: #grazie a questo metodo evito di avere la stessa mail inserita piu volte
        if email == cliente.email:
            flag_gia_esistente = True
            break
        if not flag_gia_esistente:
            clienti.append(utente)

while True:
    print("Vuoi accedere come: ")
    print("1. Cliente")
    print("2. Amministratore")
    selettore = int(input())
    
    match selettore:
        case 1:
            #Cliente
            print("1. Accedi")
            print("2. Registrati")
            
            match selettore:
                case 1:
                    #Accedi
                    print("1. Visualizza articoli disponibili")
                    print("2. Acquista un prodotto")
                    selettore = int(input())
                    
                    match selettore:
                        case 1:
                            articoli_disp = prodotti_disponibili()
                            for articolo in articoli_disp:
                                print(articolo.nome)
                        case 2:
                            
                            

                            
                            
                case 2:
                    #Registrazione
                    crea_utente() 
                case _:
                    print("Scelta non valida")
        case 2:
            #Amministratore