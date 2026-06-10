class Automobile:
    def __init__(self, targa):
        if Garage.formato_targa_valido(targa):  #grazie a quel metodo statico di Garage sono certo di avere solo targhe italiane
            self.targa = targa
    

class Garage:
    
    #capienza int
    #auto_presenti = []
    
    def __init__(self, capienza):
        self.capienza = capienza
        self.auto_presenti = []
    

    def parcheggia(self):
        if self.capienza - len(self.auto_presenti) > 0: #c'è posto nel garage?
            print("Inserisci targa auto")
            targa = input
            #il controllo sulla correttezza della targa lo faccio a monte nella creazione dell'auto, cosi faccio entrare solo targhe italiane
            auto = Automobile(targa)    #a questo punto istanzio...
            self.auto_presenti.append(auto)     #..e inserisco
        else:
            print("Posti esauriti")
    
    def rimuovi(self):
        print("Inserire targa auto da rimuovere")
        targa = input()
        if targa in self.auto_presenti:
            self.auto_presenti.remove(targa)
            print("Targa rimossa con successo")
        else:
            print("Auto non presente")
            
        
    def stampa_posti(self):
        #metodo per stampare il numero di posti liberi
        posti_liberi = self.capienza - len(self.auto_presenti)
        print("Il numero di posti liberi è" + posti_liberi)
    
    @staticmethod
    def formato_targa_valido(targa:str):
        flag_valid = False
        n_cifre_targa = len(targa)  #ho 7 cifre nella targa?
        if n_cifre_targa == 7:
            for c in targa:  #ciclo di controllo delle 7 cifre alfanum
                if c >= 1 and c <=2: #le prime due sono caratteri?
                    if c.isalpha()
                        continue    #ogni volta skippo al passo successivo
                if c >= 3 and c <=5:
                    if c.isdigit(): #le 3 centrali sono numeri?
                        continue
                if c >= 6 and c <= 7: #le ultime due sono caratter?
                    if c.isalpha():
                        continue
                else:
                    print("Targa non valida")
                    break
        return flag_valid
            
garage = Garage(100)   #istanzio il garare con 100 posti e 0 auto

#menu
while True: #voglio rimanere dentro il ciclo fino al break previsto in 4.
    print("1. Parcheggia auto")
    print("2. Stampa posti liberi")
    print("3. Rimuovi dal garage")
    print("4. Esci")
    
    selezione = int(input())
    
    match selezione:
        case 1:
            garage.parcheggia()
        case 2:
            garage.stampa_posti()
        case 3:
            garage.rimuovi()
        case 4:
            break
        case _:
            print("Scelta non valida")