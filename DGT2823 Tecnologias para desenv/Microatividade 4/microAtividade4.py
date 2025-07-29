# Importa a biblioteca pandas
import pandas as pd

dados = pd.read_csv(
    'dados.csv', 
    sep=';', 
    engine='python', 
    encoding='utf-8'
    )

print("Primeiras 10 linhas:")
print(dados.head(10))

print("\nÚltimas 10 linhas:")
print(dados.tail(10))