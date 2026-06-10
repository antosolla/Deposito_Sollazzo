class Automobile:                           # dichiaro la classe
    
    numero_di_ruote = 4                       # attributo di classe
    
    def __init__(self, marca, modello):       # metodo costruttore

        self.marca = marca                  # attributo di istanza

        self.modello = modello              # attributo di istanza

    def stampa_info(self):                    # metodo di istanza
        
        print("L'automobile è una", self.marca, self.modello)

auto1 = Automobile("Fiat", "500")    # crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3")      # crea un altro oggetto di Automobile
#istanzio due oggetti

auto1.stampa_info()                  # stampa "L'automobile è una Fiat 500"
auto2.stampa_info()                  # stampa "L'automobile è una BMW X3"

class Persona:
    def __init__(self, nome, eta):  #modifico il costruttore parametrizzandolo
        self.nome = nome   # Attributo per memorizzare il nome
        self.eta = eta     # Attributo per memorizzare l'età
# Creazione di un oggetto Persona

p = Persona("Pippo", 30)
print(p.nome)  # Output: Pippo
print(p.eta)   # Output: 30

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
# Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)
print(risultato)  
# Output: 8

class Contatore:
    numero_istanze = 0  # Attributo di classe
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")
    
# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()
#c1 avra 0, c2 avra 1 e c3 2, ma con quel metodo invece avro il numero totale di istanze
Contatore.mostra_numero_istanze()
print(c1.numero_istanze)
# Output: Sono state create 2 istanze.
