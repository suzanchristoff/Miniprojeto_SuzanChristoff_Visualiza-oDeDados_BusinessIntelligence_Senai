import pandas as pd
import numpy as np
import matplotlib as plt

# Leitura caminho dos dados
caminho_dados = "BaseVarejoDadosBrutos.csv"
df = pd.read_csv(caminho_dados, sep= ";")

print(df.head())

colunas = ['DATA', 'CO_ID', 'CL_ID', 'CL_GENERO', 'CL_EC', 'CL_FHL', 'CL_SEG', 'PR_ID', 'PR_CAT', 'PR_NOME']

print(df.columns.tolist())

print(df.info())

# datas, clientes, produtos, categorias e valores)

print(df[['DATA', 'CO_ID', 'CL_ID', 'CL_GENERO', 'CL_EC', 'CL_FHL', 'CL_SEG', 'PR_ID', 'PR_CAT', 'PR_NOME']].head())

print(df[['DATA', 'CO_ID', 'CL_ID', 'CL_GENERO', 'CL_EC', 'CL_FHL', 'CL_SEG', 'PR_ID', 'PR_CAT', 'PR_NOME']].tail())

print(df[['DATA', 'CO_ID', 'CL_ID', 'CL_GENERO', 'CL_EC', 'CL_FHL', 'CL_SEG', 'PR_ID', 'PR_CAT', 'PR_NOME']].describe())

df = df[["DATA","CL_ID","PR_NOME","PR_CAT","PR_ID","CL_GENERO"]]

print(df.size)



