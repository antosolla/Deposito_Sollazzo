class Chef:
    
    def __init__(self):
        self.nome = input("Nome dello chef: ")
        self.specialita = input("Qual è la sua specilità: ")
        
    def __call__(self, *args, **kwds):
        return self.nome

class Piatto:
    #classe piatto, con nome del piatto e relativo prezzo
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.chef_piatto = Chef()
        
        
class Ristorante:

    def __init__(self, nome, tipo_cucina):
        #costruttore per istanziare il ristorante
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu : list[Piatto] = []   #in questa maniera con vscode posso vedere metodi e attributi

    def descrivi_ristorante(self):
        #semplice metodo che da un messaggio di benvenuto e stampa i due attributi di istanza
        print(f"Benvenuti a {self.nome}, serviamo una cucina di tipo: {self.tipo_cucina}")
        
    def stato_apertura(self):
        #metodo che verifica lo stato di apertura del ristorante
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Chiuso. A domani!")
    
    
    #apri e chiudi ristorante sono duali tra loro, entrambi integrano controllo sullo stato del ristorante, riportanto errore qualora esso sia gia chiuso/aperto
    def apri_ristorante(self):
        if self.aperto:
            print("Il ristorante è gia aperto")
        else:
            print("Il locale è ora aperto!")
    
    def chiudi_ristorante(self):
        if not self.aperto:
            print("Il ristorante è gia chiuso")
        else:
            print("Il locale è ora chiuso!")
            
    def aggiungi_al_menu(self):
        print("Nome del piatto da aggiungere: ")
        nome_piatto = input()
        print("Inserisci prezzo del piatto: ")
        prezzo_piatto = input()
        #istanzio un piatto temporaneo da inserire in lista
        piatto_da_aggiungere = Piatto(nome_piatto, prezzo_piatto)
        self.menu.append(piatto_da_aggiungere)
    
    def togli_dal_menu(self):
        print("Nome del piatto da rimuovere: ")
        nome_piatto = input()
        flag_trovato = False
        for piatto in self.menu:    #itero ogni piatto, cosi da poter accedere al campo nella if successiva
            if nome_piatto == piatto.nome:  #confronto una stringa con una stringa e NON con un oggetto
                self.menu.remove(piatto)
                print("Piatto rimosso")
                flag_trovato = True
        if not flag_trovato:
            print("Piatto non presente nel menu")
                
    def stampa_menu(self):
        print("Menu:")
        for piatto in self.menu:    #itero ogni piatto, cosi da poter accedere al campo nella if successiva
            print(piatto.nome)
            
    def chi_lha_fatto(self):
        print("Di quale piatto vuoi sapere lo chef?")
        nome_piatto = input()
        for piatto in self.menu:    #verifico che il piatto sia presente in menu, magari qui potevo fare una funzione, ma il tempo è quello che è
            if nome_piatto == piatto.nome:
                print(f"Il nome dello chef è: {piatto.chef_piatto()}")  #qui uso il dunder modificato per returnare il nome, non ricordo come si concatenao le stringhe, senno avrei fatto una print nel __call__

    
ristorante = Ristorante("U' vulesce", "Pugliese")   #creo il locale

ristorante.descrivi_ristorante()
#ciclo for per inserire tre piatti
"""for i in range(3):
    ristorante.aggiungi_al_menu()
    
 ristorante.stato_apertura()

ristorante.apri_ristorante()

ristorante.chiudi_ristorante()

ristorante.chiudi_ristorante()  #provo a chiuderlo di nuovo per testare l'if

ristorante.togli_dal_menu()

ristorante.stampa_menu() """
ristorante.aggiungi_al_menu()
ristorante.chi_lha_fatto()





    