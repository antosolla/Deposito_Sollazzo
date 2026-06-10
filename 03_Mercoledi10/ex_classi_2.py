class Libro:

    
    def __init__(self, titolo, autore, pagine): #modifico il costruttore in maniera tale che, in fase di istanziazione possa avere gia dei valori, probabilmente posso togliere quelle due assegnazioni
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        

    
while True:
    titolo = input("Inserisci nome libro")
    autore = input("Inserisci autore libro")
    pagine = input("Inserisci numero di pagine del libro")
    
    libro = Libro(titolo, autore, pagine)
    biblioteca = []
    biblioteca.append(libro)
    print("Libro aggiunto. Vuoi continuare?")
    risposta = input()
    if 
    
    