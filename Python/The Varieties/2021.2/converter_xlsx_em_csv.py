# Início →

# pip install pandas
# pip install openpyxl

import pandas as pd

def converte_para_csv(nome_arquivo):
    df = pd.read_excel(nome_arquivo)
    csv = nome_arquivo.split('.')[0] + '.csv'
    df.to_csv(csv, encoding='utf-8', sep=';', index=False)
    return csv

nome_arquivo = input('Digite o nome do arquivo Excel: ')
converte_para_csv(nome_arquivo + '.xlsx')

# ← Fim