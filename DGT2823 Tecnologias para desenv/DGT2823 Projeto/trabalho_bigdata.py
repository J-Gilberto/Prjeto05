# tratamento_dados.py
# Autor: João Gilberto e com ajuda da ferramenta Git Copilot
# Objetivo: Limpeza e preparação de dados para análise usando Pandas

import pandas as pd
import numpy as np

print("\n--- PASSO 1: Preparação do dataset ---")
# PASSO 1: Preparação do dataset
sample_data = """ID;Duration;Date;Pulse;Maxpulse;Calories
0;60;'2020/12/01';110;130;4091
1;60;'2020/12/02';117;145;4790
2;60;'2020/12/03';103;135;3400
3;45;'2020/12/04';109;175;2824
4;45;'2020/12/05';117;148;4060
5;60;'2020/12/06';102;127;3000
6;60;'2020/12/07';110;136;3740
7;450;'2020/12/08';104;134;2533
8;30;'2020/12/09';109;133;1951
9;60;'2020/12/10';98;124;2690
10;60;'2020/12/11';103;147;3293
11;60;'2020/12/12';100;120;2507
12;60;'2020/12/12';100;120;2507
13;60;'2020/12/13';106;128;3453
14;60;'2020/12/14';104;132;3793
15;60;'2020/12/15';98;123;2750
16;60;'2020/12/16';98;120;2152
17;60;'2020/12/17';100;120;3000
18;45;'2020/12/18';90;112;NaN
19;60;'2020/12/19';103;123;3230
20;45;'2020/12/20';97;125;2430
21;60;'2020/12/21';108;131;3642
22;45;NaN;100;119;2820
23;60;'2020/12/23';130;101;3000
24;45;'2020/12/24';105;132;2460
25;60;'2020/12/25';102;126;3345
26;60;20201226;100;120;2500
27;60;'2020/12/27';92;118;2410
28;60;'2020/12/28';103;132;NaN
29;60;'2020/12/29';100;132;2800
30;60;'2020/12/30';102;129;3803
31;60;'2020/12/31';92;115;2430"""

# Gravar CSV na pasta local
with open('dados.csv', 'w', encoding='utf-8') as f:
    f.write(sample_data)



df_original = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# PASSO 2: Novo arquivo/script (já criado)
print("\n--- Passo 2: Novo script criado ---")
# 2️ Informações gerais do dataset
print("\n Informações gerais do DataFrame original:")
print(df_original.info())
print("\n Primeiras 5 linhas:")
print(df_original.head())
print("\n Últimas 5 linhas:")
print(df_original.tail())

# PASSO 3: Leitura dos dados
print("\n--- PASSO 3: Leitura dos dados ---")
# 3️ Cópia dos dados originais
df_tratado = df_original.copy()

# PASSO 4: Verificação da coluna 'Calories'
print("\n--- PASSO 4: Tratamento da coluna 'Calories' ---")
print("\nColunas disponíveis:\n", list(df_tratado.columns))
# 4️ Substituir nulos da coluna 'Calories' por 0
df_tratado['Calories'].fillna(0, inplace=True)

# PASSO 5: Verificação da coluna 'Date'
print("\n--- PASSO 5: Tratamento da coluna 'Date' ---")
# 5️ Substituir nulos da coluna 'Date' por '1900/01/01'
df_tratado['Date'].fillna('1900/01/01', inplace=True)

#PASSO 6: Tentativa de conversão da coluna 'Date' para datetime
print("\n--- PASSO 6: Tentativa de conversão da coluna 'Date'---")
# 6️ Substituir '1900/01/01' por NaN
df_tratado['Date'].replace('1900/01/01', np.nan, inplace=True)

#PASSO 7: Conversão da coluna 'Date' para datetime
print("\n--- PASSO 7: Conversão da coluna 'Date' para datetime ---")
# 7️ Corrigir valor '20201226' para formato datetime
df_tratado['Date'] = df_tratado['Date'].replace('20201226', '2020-12-26')

#PASSO 8: Conversão final da coluna 'Date'
print("\n--- PASSO 8: Conversão final da coluna 'Date' ---")
# 8️ Detectar formatos automaticamente e converter para datetime
df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], errors='coerce', infer_datetime_format=True)

# PASSO 9: Verificação final das datas tratadas
print("\n--- PASSO 9: Verificação final das datas tratadas ---")
# 9️ Verificar resultados após conversão
print("\n Datas tratadas:")
print(df_tratado['Date'])

# PASSO 10: Exibir DataFrame tratado
print("\n DataFrame tratado:")
#  Confirmar conversão de todas as datas (nova tentativa já feita acima)
# (Etapa já concluída com o uso de infer_datetime_format)

#PASSO 11: Exibir DataFrame completo tratado antes da remoção de nulos
print("\n DataFrame tratado antes da limpeza final:")
# 1️1️ Exibir DataFrame completo tratado antes da remoção de nulos
print(df_tratado)

# PASSO 12: Remover registros com valores nulos
print("\n--- PASSO 12: Removendo registros com valores nulos ---")
# 1️2️ Remover registros com valores nulos (como datas inválidas)
df_final = df_tratado.dropna()

#PASSO 13: Exibir DataFrame final tratado
print("\n--- PASSO 13: DataFrame final tratado ---")
# 1️3️ Exibir e salvar DataFrame final tratado
print("\n DataFrame final após remoção de nulos:")
print(df_final)

#PASSO 14: Exportar DataFrame tratado para CSV
print("\n--- PASSO 14: Exportando DataFrame tratado para CSV ---")
# (Extra) Exportar para novo arquivo CSV
df_final.to_csv('dados_tratados.csv', index=False)
print("\n Arquivo 'dados_tratados.csv' gerado com sucesso!")