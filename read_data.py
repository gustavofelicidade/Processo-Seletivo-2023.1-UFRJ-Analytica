import os
import csv
import pandas as pd
import logging
import time
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Análise exploratória

# Ler a página "2002" do arquivo
# Tabela 1686 - Consumo total mensal de energia elétrica, segundo classe de serviço - Município do Rio de Janeiro - 2019
df1 = pd.read_excel(
    r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Originals\1686.xls",
    sheet_name="2002", header=6, skiprows=2, nrows=12)

# Ler a página "T 2257" do arquivo
# "Tabela 2257 - Consumo total, médio anual, mensal e diário
# de energia elétrica por habitante no Município do Rio de Janeiro
# entre  1980-2019"
df2 = pd.read_excel(
    r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Originals\2257.xls",
        sheet_name="T 2257", header=6, skiprows=1, nrows=40)

# Imprimir os DataFrames
# print("Tabela 2257 - Consumo total, médio anual, mensal e diário \n de energia elétrica por habitante no Município do Rio de Janeiro entre  1980-2019")
# print(df2)



def collect_dataframes(file_path):
    # criar uma lista vazia para armazenar os dataframes de cada ano
    df_list = []
    # percorrer os anos de 2002 a 2019
    for year in range(2002, 2020):
        # criar o nome da sheet com base no ano
        sheet_name = str(year)
        # ler o dataframe da sheet especificada
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=6, skiprows=2, nrows=12)
        # adicionar o dataframe à lista
        df_list.append(df)
    # retornar a lista de dataframes
    return df_list

file_path = r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Originals\1686.xls"
df_list = collect_dataframes(file_path)
# print(df_list)
df_2002 = df_list[0]

# logger.info(f"df_list: {df_list}")
# #
# logger.info(f"df_2002: {df_2002}")
#
# def print_second_column(df_list):
#     # percorrer cada dataframe na lista
#     for df in df_list:
#         # selecionar a segunda coluna e imprimir
#         print(df.iloc[:, ])

# print_second_column(df_list)

# Tabela 1686
# Coluna Residência -
def print_third_column(df_list):
    # percorrer cada dataframe na lista
    for df in df_list:
        # selecionar a terceira coluna e imprimir
        print(df.iloc[:, 2])

print_third_column(df_list)




# selecionar a coluna "Residencial" de todos os dataframes na lista
residencial_list = [df.iloc[:, 2] for df in df_list]
# print("residencial_list")
# print(residencial_list)
# populacao = df2.iloc[:, 5]
# print("populacao")
# print(populacao)


pio.renderers.default = 'browser'
# Gráfico de linha para população
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df2.iloc[:, 0], y=df2.iloc[:, 5], name='População'))

# Gráfico de barras para consumo residencial
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=[str(year) for year in range(2002, 2020)], y=[df.iloc[:, 2].sum() for df in df_list], name='Consumo residencial'))

# Criar um mesmo gráfico com os dois plots
fig = make_subplots(rows=1, cols=2, shared_xaxes=True)
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)

# Configurar o layout
fig.update_layout(title='População e consumo residencial do Rio de Janeiro (2002-2019)',
                  xaxis_title='Ano',
                  yaxis_title='População / Consumo residencial (MWh)')

# Mostrar o gráfico
fig.show()

