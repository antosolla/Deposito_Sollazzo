class Libro:
    
    def __init__(self, titolo, autore, pagine): #modifico il costruttore in maniera tale che, in fase di istanziazione possa avere gia dei valori, probabilmente posso togliere quelle due assegnazioni
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def stampa_titolo(self):
        print(self.titolo)
        
biblioteca : list[Libro] = []  #la lista va definita in questo modo, per una questione di type  hint
while True:
    titolo = input("Inserisci titolo libro")
    autore = input("Inserisci autore libro")
    pagine = input("Inserisci numero di pagine del libro")
    libro = Libro(titolo, autore, pagine)
    biblioteca.append(libro)
    print("Libro aggiunto. Scrivi no se non vuoi continuare?")
    risposta = input()
    risposta.lower()
    if risposta == "no":
        break

for elemento in biblioteca:
    elemento.stampa_titolo()    #dopo la questione type hint vs code mi ha suggerito metodo
