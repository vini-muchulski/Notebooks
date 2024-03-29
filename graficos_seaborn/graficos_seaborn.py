# -*- coding: utf-8 -*-
"""graficos_seaborn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/119y-IwwB94YXrT8-6z8PgZ-gHtOLNvTx
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("videosYT.xlsx")
df



fig = sns.scatterplot(data=df,x="Nº de Views",
 y="Nº de Likes",hue="Categoria")
plt.show(fig)

fig = sns.scatterplot(data=df,x="Nº de Views",
 y="Nº de Likes",hue="Categoria",style="Responsável")
plt.show(fig)

df = pd.read_excel("videosYT.xlsx", "Inscritos")
df

fig = sns.lineplot(data=df, x = "Mês/Ano", y = "Inscritos",color="green")
plt.show(fig)

#voltando para o df antigo
fig = sns.displot(data=df,x="Nº de Views")

fig = sns.displot(data=df,x="Nº de Views", kind = "kde")

graf_regressao_linear = sns.regplot(data=df,x="Nº de Views",
 y="Nº de Likes")

graf_regressao_linear = sns.lmplot(data=df,x="Nº de Views",
 y="Nº de Likes",hue="Responsável")
plt.show(fig)