#dunder methods
#str
class Studente:
 def __init__(self, nome, eta):
   self.nome = nome
   self.eta = eta

 def __str__(self):
   return "Studente: " + self.nome + ", età: " + str(self.eta)

studente1 = Studente("Luca", 20)
print(studente1)

#esempio len
class Squadra:
    def __init__(self, nome, giocatori):
        self.nome = nome
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)

squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])
print(len(squadra1))


#call
class Moltiplicatore:
 def __init__(self, numero):
    self.numero = numero
 def __call__(self, valore):  #motivi di sicurezza informatica, non è visibile lato utente, non so nemmeno come si chiama la funzione
    return valore * self.numero

doppio = Moltiplicatore(2)
print(doppio(10))


#eq
class Prodotto:
  def __init__(self, nome, prezzo):
    self.nome = nome
    self.prezzo = prezzo

  def __eq__(self, altro):
    return self.nome == altro.nome and self.prezzo == altro.prezzo

prodotto1 = Prodotto("Mouse", 20)
prodotto2 = Prodotto("Mouse", 20)
prodotto3 = Prodotto("Tastiera", 35)
print(prodotto1 == prodotto2) #cìè un eq percio viene richiamato il metodo eq
print(prodotto1 == prodotto3)