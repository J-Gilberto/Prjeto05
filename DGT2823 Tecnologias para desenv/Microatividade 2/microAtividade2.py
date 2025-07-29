# Adicionando as 3 tabelas de dados
import pandas as pd

caminho_arquivo = 'dados.csv'

dados = pd.read_csv(
    caminho_arquivo, sep=';', 
    engine='python', 
    encoding='utf-8'
    )


print("Colunas disponíveis:")
print(dados.columns)

subconjunto = dados[['ID', 'Duration', 'Calories']]

print("\nSubconjunto de dados:")
print(subconjunto)