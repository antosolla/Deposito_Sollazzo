import modulo_libreria
import modulo_Libro

#prima di tutto creo una libreria

libreria = modulo_libreria.Libreria()

print("Fase di inserimento: ")
for i in range(3):
    titolo = input("Nome del libro: ")
    autore = input("Autore del libro: ")
    isbn = input("ISBN del libro: ")

    libro_da_inserire = modulo_Libro.Libro(titolo, autore, isbn)
    