'''Traccia progetto:

Partendo da questo dataframe su kaggle [link dataset](https://www.kaggle.com/datasets/fedesoriano/the-boston-houseprice-data) 

1. Caricare i dati in un DataFrame
2. Visualizzare le prime e le ultime cinque righe del DataFrame
3. Visualizzare il tipo di dati di ciascuna colonna
4. Calcolare statistiche descrittive di base per le colonne numeriche
5. verificate se ci sono correlazioni 
6. calcolate la media dei prezzi delle case raggruppati per un variabile categorica creata sulla base delle stranze della casa e realizzate grafici esplicativi
7. eseguite le seguenti analisi:

- Esplorazione delle relazioni tra categorie e prezzo di vendita: Esamina come il prezzo di vendita varia in base alle variabili categoriche

- Analisi delle caratteristiche di località: Esplora le caratteristiche di località (fiume, vicinanza lavoro) e analizza come influenzano il prezzo di vendita.'''

#1
import pandas as pd
df = pd.read_csv('boston.csv')

df.head()
