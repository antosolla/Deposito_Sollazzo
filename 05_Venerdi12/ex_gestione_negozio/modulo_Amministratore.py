class Amministratore:
    
    n_admin = 0
    
    def __init__(self, nome_cognome, email, password):
        self.nome_cognome = nome_cognome
        self.email = email
        self.password = password
        self.id_cliente = Amministratore.conta_admin() + 1 #in questo modo ho un intero incrementale, grazie al metodo statico che prima mi conta i clienti e poi assegna un +1 a tale valore    
    
    @classmethod
    def conta_admin(cls):
        return cls.n_admin