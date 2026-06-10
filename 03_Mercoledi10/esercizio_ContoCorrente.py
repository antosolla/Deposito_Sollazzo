class ContoCorrente:

    def __init__(self, intestatario, saldo=0):
        self.intestatario = intestatario
        self.saldo = saldo
    
    def deposita(self):
        print("Quanto vuoi depositare?")
        somma_deposito = int(input())
        self.saldo = self.saldo + somma_deposito
    
    #questo decoratore fa si che si eviti di entrare nella procedura di prelievo se il saldo è negativo o uguale a zero
    def check_saldo_negativo(func):
        def wrapper(self):
            if self.saldo <= 0:
                print("Il tuo saldo è insufficiente, non puoi prelevare")
            else:
                func()  #altrimenti passo alla procedura di prelievo, che poi sia insufficiente eventualmente è un problema ell'if sotto
            return wrapper
    #applico decoratore alla funzione preleva
    @check_saldo_negativo
    def preleva(self):
        print("Quanto vuoi prelevare?")
        somma_prelievo = int(input())
        if somma_prelievo > self.saldo:
            print("La somma da prelevare è piu alta della tua disponibilità")
        else:
            self.saldo = self.saldo - somma_prelievo
    
    def stampa_saldo(self):
        print(f"Il saldo di {self.intestatario} è: {self.saldo}€")

lista_conti: list[ContoCorrente] = []   
#cosi posso vedere i metodi che ci sono dentro

while True: #voglio rimanere dentro il ciclo fino al break previsto in 5.
    print("1. Crea conto")
    print("2. Deposita")
    print("3. Preleva")
    print("4. Stampa saldo")
    print("5. Esci")
    
    selezione = int(input())
    
    match selezione:
        case 1:
            print("Inserisci il nome dell'intestatario")
            nome=input()
            lista_conti.append(ContoCorrente(nome)) #richiamo metodo costruttore direttamente dentro append
            print("Utente creato con successo") 
        case 2:
            print("Inserisci il nome dell'intestatario su cui depositare")
            nome=input()
            indice=lista_conti.index(nome) #ottengo indice del nome associato
            lista_conti[indice].deposita()  #una volta ottenuto indice, posso richiamare il metodo di istanza
        case 3:
            print("Inserisci il nome dell'intestatario da cui prelevare")
            nome=input()
            indice=lista_conti.index(nome) #ottengo indice del nome associato
            lista_conti[indice].preleva()
        case 4:
            print("Di quale intestatario vuoi stampare il saldo?")          
            nome=input()
            indice=lista_conti.index(nome)  #ottengo indice del nome associato
            lista_conti[indice].stampa_saldo()
        case 5:
            break
        case _:
            print("Scelta non valida")