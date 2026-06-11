class Convertitore:
    
    @staticmethod
    def euro_in_dollari(euro):  #metodo per la conversione eur-usd
        return euro*1.08
    
    @staticmethod
    def km_in_miglia(km):   #metodo per la conversione km --> miglia
        return km*0.621371

#per testare correttamente passo il valore 1, se corrisponde al tasso di conversione, allora è ok
#ho richiamato funzioni direttamente dalla funzione print
print(f"L'importo convertito in dollari corrisponde a:{Convertitore.euro_in_dollari(1)}")
print(f"La lunghezza convertita in miglia corrispondena: {Convertitore.km_in_miglia(1)}")