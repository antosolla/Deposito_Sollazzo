class Punto:
    dx = 0
    dy = 0
    
    def __init__(self, dx, dy): #modifico il costruttore in maniera tale che, in fase di istanziazione possa avere gia dei valori, probabilmente posso togliere quelle due assegnazioni
        self.dx = dx
        self.dy = dy
        
    def muovi(self, dx, dy):    #prendo in input i valori ed aggiorno gli attributi di istanza
        self.dx = dx
        self.dy = dy
    
    def distanza_da_origine(self):
        distanza = abs(((self.dy**2)-(self.dx)**2)**0.5)    #la distanza NON puo essere negativa, uso valore assoluto percio
        return distanza
    
p1 = Punto(15,5)    #istanzio l'oggetto
p1.muovi(5,0)       #richiamo il metodo per muovere
print(p1.distanza_da_origine()) #stampo il valore del metodo/funzione