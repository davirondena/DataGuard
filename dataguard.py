import os
import pandas as pd

folder_path = 'C:/Users/Davi Rondena/Downloads/lambda/dadosCSV'

def read_s_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, header=0)
    return df

def read_csvs(folder_path):
    arquivos = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    list_df = []
    for arq in arquivos:
        caminho = os.path.join(folder_path, arq)
        df = read_s_csv(caminho)
        list_df.append(df)
    return list_df

dfs = read_csvs(folder_path)
for df in dfs:
    print(df.head())


