# -*- coding: utf-8 -*-
"""apic-bacen_selic_cdi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Z1qhGBE-Nr5KmJeeoHOYwu9QqpHFexi
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
#https://www.youtube.com/watch?v=pZlsfaVk7c0&list=PLP_dh3S9H39kSv9Ke0Ezie8HAlm5zfVhc&index=2
#https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
# bcb https://wilsonfreitas.github.io/python-bcb/

hoje = date.today()
hoje

"""#Importando e extração da selic"""

data_start = "01/01/2018"
data_fim = f"{hoje.day}/{hoje.month}/{hoje.year}"
link = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={data_start}&dataFinal={data_fim}"
print(data_fim)

df = pd.read_json(link)
df.set_index("data",inplace=True)
df

df.index = pd.to_datetime(df.index, dayfirst=True)

display(df)
df.plot()

"""#Generalização do codigo -> IPCA, CDI

"""

data_start = "01/01/2018"
data_fim = f"{hoje.day}/{hoje.month}/{hoje.year}"
dado = "432"
link = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{dado}/dados?formato=json&dataInicial={data_start}&dataFinal={data_fim}"

def extracao_bacen(data_start,data_fim,dado):
  link = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{dado}/dados?formato=json&dataInicial={data_start}&dataFinal={data_fim}"
  df = pd.read_json(link)
  df.set_index("data",inplace=True)
  df.index = pd.to_datetime(df.index, dayfirst=True)
  return df

df_ipca = extracao_bacen(dado="433",data_start=data_start,data_fim=data_fim) #433 ->ipca
df_ipca.plot()

df_cdi = extracao_bacen(dado="4389",data_start=data_start,data_fim=data_fim) #4389 ->cdi
df_cdi.plot()

display(df_cdi)

import seaborn as sns
import numpy as np

sns.lineplot(data=df_cdi)
plt.yticks(np.arange(0, df_cdi['valor'].max(), step=0.5))
plt.tight_layout()

"""#Extras"""

pip install mplcyberpunk

pip install python-bcb

import mplcyberpunk
import matplotlib.ticker as mtick

#df_cdi

plt.style.use("cyberpunk")
df_cdi.plot()