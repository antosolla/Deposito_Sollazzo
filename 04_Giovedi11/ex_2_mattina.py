class Animale:
    numero_animali = 0  #non è attributo di istanza, bensi di classe, ovvero condiviso da tutte le istanze
    
    def __init__(self, nome, specie):
        Animale.numero_animali += 1 #per ogni istanza creata, aumento il contatore di animali di 1
        self.nome = nome    #questi due sono invece di istanza, differenti per ogni animale inserito
        self.specie = specie
        
    @classmethod    #passo per paramentro la classe stessa
    def quanti_animali(cls):
        print(f"Sono presenti {cls.numero_animali} animali")    #per fare riferimento all'attributo di classe, non usero self, ma cls
        
#istanzio tre animali
animale1 = Animale("Bob", "Gatto")
animale2 = Animale("Spirit", "Cavallo")
animale3 = Animale("Nemo", "Pesce")
#infine richiamo il metodo di classe
Animale.quanti_animali()
