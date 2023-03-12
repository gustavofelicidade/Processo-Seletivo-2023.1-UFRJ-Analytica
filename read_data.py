
import os
import csv
import pandas as pd
import logging
import time
import matplotlib
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ler a página "Sheet1" do arquivo "exemplo.xls"
df1 = pd.read_excel(
    r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Originals\1686.xls",
    sheet_name="2002", header=6, skiprows=2, nrows=12)

# Ler a página "Sheet2" do arquivo "exemplo.xls"
df2 = pd.read_excel(
    r"D:\Arquivos HD\Documentos HD\biblioteca\Matematica\UFRJ Analytica\Processo Seletivo 2023.1\Originals\1687.xls",
    sheet_name="2002", header=5, skiprows=1)

# Imprimir os DataFrames
print(df1)
# print(df2)