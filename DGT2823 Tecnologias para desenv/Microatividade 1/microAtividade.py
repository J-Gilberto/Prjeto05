# Importando a biblioteca pandas
import pandas as pd

caminho_arquivo = 'dados.csv'

dados = pd.read_csv(
    caminho_arquivo,
    sep=',',             
    engine='python',
    encoding='utf-8'      
)

print(dados)

