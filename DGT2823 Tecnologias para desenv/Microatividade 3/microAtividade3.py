# Importar biblioteca pandas
import pandas as pd

pd.options.display.max_rows = 9999

dados = pd.read_csv(
    'dados.csv', 
    sep=';', 
    engine='python', 
    encoding='utf-8'
    )

print(dados.to_string())