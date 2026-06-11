import modulo_Libro

class Libreria:
    
    def __init__(self):
        self.catalogo : list[modulo_Libro.Libro] = []   #prima accedo al modulo, poi al suo interno
        #in ogni caso, istanzio un catalogo vuoto
        
    def aggiungi_libro(self, libro:modulo_Libro.Libro):   #specifico il tipo dell'oggetto da ricevere
        self.catalogo.append(libro)
        print("Libro inserito con successo")
        
    def rimuovi_libro(self):
        trovato = False #flag per l'if finale, di controllo, se falso, il libro non è presente, vero se il contrario
        isbn_libro_da_eliminare = input("Inserire ISBN del libro da eliminare: ")
        for libro in self.catalogo:
            if isbn_libro_da_eliminare == libro.isbn:
                self.catalogo.remove(libro) #passare come argomento un oggetto e non una stringa!
                trovato = True
            else:
                trovato = False
        if not trovato:
            print("Libro non presente in catalogo")
        else:
            print("Libro trovato ed eliminato dal catologo")
            
    def cerca_per_titolo(self):
        titolo_da_cercare=input("Inserire titolo del libro da cercare: ")
        for libro in self.catalogo:
            if titolo_da_cercare in libro.titolo:   #stampo tutti i libri la cui stringa da cercare sia nella stringa dei titoli del catalogo
                print(libro.titolo)
                
    def mostra_catalogo(self):
        print("Lista dei libri presenti in catalogo")
        for libro in self.catalogo:   #stampo tutti i libri
                print(libro.titolo)
                
