'''Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 
1.Caricare i dati in un DataFrame autogenerandoli casualmente .
2.Visualizzare le prime e le ultime cinque righe del DataFrame.
3.Visualizzare il tipo di dati di ciascuna colonna.
4.Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
5.Identificare e rimuovere eventuali duplicati.
6.Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
7.Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior)'''

import pandas as pd

# Generare dizionario con dati casuali

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Età': [25, 30, 35, null, 45, 50, 55, 60, 65, 70],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Palermo', 'Genova', 'Bologna', 'Firenze', 'Venezia', 'Verona'],
    'Salario': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000]
}

# 1. Creare DataFrame
df = pd.DataFrame(data)

# 2. Visualizzare le prime e le ultime cinque righe del DataFrame
print("Prime cinque righe del DataFrame:")
print(df.head())
print("Ultime cinque righe del DataFrame:")
print(df.tail())

# 3. Visualizzare il tipo di dati di ciascuna colonna
print("Tipo di dati di ciascuna colonna:")
print(df.dtypes)

# 4. Calcolare statistiche descrittive di base per le colonne numeriche
print("Statistiche descrittive di base per le colonne numeriche:")
print(df.describe())
#output: count, mean, std, min, 25%, 50%, 75%, max

# 5. Identificare e rimuovere eventuali duplicati
df = df.drop_duplicates()


# 6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna
df_modificato = df.fillna({'Età': df['Età'].median(), 'Salario': df['Salario'].median()})
#senza inplace=true, quindi non modifica il df originale, ma restituisce una copia modificata

# 7. Aggiungere una nuova colonna chiamata "Categoria Età"
for element in df_modificato['Età']:
    if element <= 18:
        df_modificato["Categoria Età"] = 'Giovane'
    elif 19 <= element <= 65:
        df_modificato["Categoria Età"] = 'Adulto'
    else:
        df_modificato["Categoria Età"] = 'Senior'

print(df)
print("\n")
print(df_modificato)
