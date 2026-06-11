class Libro:
    
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f"Il titolo del libro è: {self.titolo}, è stato scritto da: {self.autore} ed il suo ISBN è: {self.isbn}")
        
    
    