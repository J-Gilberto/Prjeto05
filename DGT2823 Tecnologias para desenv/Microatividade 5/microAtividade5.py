import pandas as pd

dados = pd.read_csv(
    'dados.csv', 
    sep=';', 
    engine='python', 
    encoding='utf-8'
    )

print("Informações gerais:")
dados.info()

linhas, colunas = dados.shape
print(f"\nTotal de linhas: {linhas}")
print(f"Total de colunas: {colunas}")

print("\nQuantidade de dados nulos por coluna:")
print(dados.isnull().sum())

print("\nTipos de dados das colunas:")
print(dados.dtypes)

memoria = dados.memory_usage(deep=True).sum()
print(f"\nMemória utilizada pelo conjunto: {memoria} bytes")