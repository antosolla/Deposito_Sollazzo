import pandas as pd

data = {
    'Prodotto': ['Uva', 'Mela', 'Uva', 'Arancia', 'Ciliegia', 'Pesca', 'Ciliegia', 'Kiwi', 'Kiwi', 'Ananas'],
    'Quantità': [10, 20, 15, 25, 30, 12, 18, 22, 28, 35],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Palermo', 'Napoli', 'Bologna', 'Napoli', 'Venezia', 'Verona'],
    'Prezzo Unitario': [1, 4, 6, 4, 3, 5, 7, 2, 8, 9]
}

dataframe = pd.DataFrame(data)


dataframe['Totale Vendite'] = dataframe["Prezzo Unitario"] * dataframe["Quantità"]
#basta fare un prodotto, non ho bisogno di for
print(dataframe['Totale Vendite'])

print(dataframe["Prodotto"])
#stampo tutti i prodotti
print(dataframe.groupby("Prodotto", as_index=False)["Totale Vendite"].sum())    #raggruppo per prodotto e sommo le vendite totali

vendite_per_citta = dataframe.groupby("Città")["Totale Vendite"].sum()
id_vendita_citta = vendite_per_citta.idxmax()
value_vendita_citta = vendite_per_citta.max()

print("\nProdotto piu venduto in termini di quantita:")
print(f"{id_vendita_citta}: {value_vendita_citta} unita")




id_max_prodotto = dataframe.groupby("Prodotto", as_index=False)["Totale Vendite"].sum().idxmax()
valore_max_prodotto = dataframe.groupby("Prodotto", as_index=False)["Totale Vendite"].sum().max()
#ora ho indice e valore massimo, posso stampare il prodotto piu venduto
print("Prodotto piu venduto:", dataframe.loc[id_max_prodotto, "Prodotto"], "con vendite totali di:", valore_max_prodotto)
# il loc mi permette di accedere a una riga specifica del dataframe in base all'indice, e poi seleziono la colonna "Prodotto" per ottenere il nome del prodotto piu venduto.

#la citta con il maggior numero di vendite totali
id_max_citta = dataframe.groupby("Città", as_index=False)["Totale Vendite"].sum()["Totale Vendite"].idxmax()
valore_max_citta = dataframe.groupby("Città", as_index=False)["Totale Vendite"].sum()["Totale Vendite"].max()
print("Città con il maggior numero di vendite totali:", dataframe.loc[id_max_citta, "Città"], "con vendite totali di:", valore_max_citta)
#sostanzlaimente è equivalente al group by di SQL

#costruisco un df con vendite superiori a 1000
nuovo_df = dataframe[dataframe["Totale Vendite"] > 1000]

#visualizzo numero vendite per citta
print(dataframe.groupby("Città", as_index=False)["Totale Vendite"].sum())
df_citta=dataframe["Città"].value_counts()
print(df_citta)
