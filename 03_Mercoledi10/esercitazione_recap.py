'''
Gestore di uno sportello bancario, creo tre liste, una con nome e cognome, 
una col numero di conto, l'altra con il saldo di ognuno, farò riferimento a tutt'e tre tramite indice
Creo un menu da cui posso:
1. Inserire nuovo utente (append)
2. Rimuovere utente (remove)
3. Aggiornare il saldo di un cliente (dunque operazione di prelievo o deposito)
4. Avere informazione su un cliente
5. Lista dei correntisti con saldo minore di zero (integrare generatore)
6. Patrimonio in gestione (sum)
7. Saldo medio dei correntisti (avg)
'''
nomi_cognomi = []
numeri_conto = []
saldi = []
bad_users = [] #lista che contiene indici dei correntisti con saldo negativo

#funzione che aggiunte utente
def add_user():
    nome_cognome = input("Inserisci nome e cognome del cliente: ")
    numero_conto = input("Inserisci numero di conto del cliente: ")
    saldo = float(input("Inserisci saldo del cliente: "))
    
    nomi_cognomi.append(nome_cognome)
    numeri_conto.append(numero_conto)
    saldi.append(saldo)
    print("Utente aggiunto")

#funzione che rimuove utente
def remove_user():
    nome_cognome = input("Inserisci nome e cognome del cliente da rimuovere: ")
    
    for elemento in nomi_cognomi:
        if elemento == nome_cognome:
            index = nomi_cognomi.index(elemento)
            nomi_cognomi.remove(elemento)
            numeri_conto.pop(index)
            saldi.pop(index)   #uso pop perchè remove rimuove l'elemento, pop rimuove per indice
            print("Utente rimosso")

#funzione che aggiorna il saldo di un cliente
#vedere bene come funzione decoratore, vorrei che la funzione modificasse il suo comportantemento a seconda del saldo inserito
def update_user(nome_cognome):
    print("1. Deposito")
    print("2. Prelievo")
    scelta = int(input("Scegli un'opzione: "))
    for elemento in nomi_cognomi:
        if elemento == nome_cognome:
            index = nomi_cognomi.index(elemento)
            if scelta == 1:
                deposito = float(input("Inserisci importo del deposito: "))
                saldi[index] += deposito
                print("Deposito effettuato")
            elif scelta == 2:
                prelievo = float(input("Inserisci importo del prelievo: "))
                if prelievo <= saldi[index]: #controllo che il prelievo non sia maggiore del saldo
                    saldi[index] -= prelievo
                    print("Prelievo effettuato")
                else:
                    print("Saldo insufficiente")
            else:
                print("Scelta non valida")
#funzione che restituisce le info di un cliente             
def info_user():
    nome_cognome = input("Inserisci nome e cognome del cliente: ")
    for elemento in nomi_cognomi:
        if elemento == nome_cognome:
            index = nomi_cognomi.index(elemento)
            print("Nome e cognome: ", nomi_cognomi[index])
            print("Numero di conto: ", numeri_conto[index])
            print("Saldo: ", saldi[index])

def print_bad_users():
    print("Correntisti con saldo minore di zero:")
    bad_users.append(check_negative_balance(saldi)) #riceve dal generatore i saldi negativi
    print(bad_users) #stampo la lista dei saldi negativi

def check_negative_balance(saldi):
    for saldo in saldi:
        if saldo < 0:
            yield saldo #generatore che restituisce SOLO i saldi negativi 

def total_sum_users():
    total_sum = sum(saldi)
    print("Patrimonio in gestione: ", total_sum)

def avg_users():
        avg = sum(saldi) / len(saldi)
        print("Saldo medio dei correntisti: ", avg)

while True:
    print("Menu:")
    print("1. Inserire nuovo utente")
    print("2. Rimuovere utente")
    print("3. Aggiornare il saldo di un cliente")
    print("4. Avere informazione su un cliente")
    print("5. Lista dei correntisti con saldo minore di zero")
    print("6. Patrimonio in gestione")
    print("7. Saldo medio dei correntisti")
    print("8. Esci")

    scelta = int(input("Scegli un'opzione: "))

    match scelta:
        case 1:
            add_user()
        case 2:
            remove_user()
        case 3:
            nome_cognome = input("Inserisci nome e cognome del cliente: ")
            update_user(nome_cognome)
        case 4:
            info_user()
        case 5:
            print_bad_users()
        case 6:
            total_sum_users()
        case 7:
            avg_users()
        case 8:
            print("Chiusura del programma")
            break
        case _:
            print("Scelta non valida.")