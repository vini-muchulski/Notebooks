# -*- coding: utf-8 -*-
"""api_acoes_e_infosEconomicas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dn6Iwss0PXwlh2kKuNnPexg9Z7sj86LG

# API de Preço de Ações e Informações Econômicas com Python
## Video = https://www.youtube.com/watch?v=oIhrwXDbs1M
### Doc: https://www.alphavantage.co/documentation/#weeklyadj
"""

chave_api = "NJCF0G5KKOKB1ID9"

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

#simbolo da acao deve ser equivalente ao do yahoo finance
#https://finance.yahoo.com/quote/MSFT?.tsrc=fin-srch
simbolo = "BPAC11.SAO"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={simbolo}&apikey={chave_api}'

r = requests.get(url)
data = r.json()

print(data)

"""Pegando cotacoes semanais - CSV

"""

import pandas as pd
from io import StringIO # pega texto e transforma em arquivo

simbolo = "BPAC11.SAO"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={simbolo}&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
display(tabela)
#print(r.text)



"""Várias cotações

"""

acoes = ["BPAC11.SAO","WEGE3.SAO","EGIE3.SAO"]

compilada = pd.DataFrame()

for acao in acoes:
  url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}&apikey={chave_api}&datatype=csv'
  r = requests.get(url)

  tabela = pd.read_csv(StringIO(r.text))
  lista_tabelas = [compilada, tabela]
  compilada = pd.concat(lista_tabelas)

display(compilada)

"""# encontar ativos
Search Endpoint
"""

simbolo = "VALE"
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={simbolo}&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
display(tabela)

"""# resultados

"""

#simbolo = "BPAC11.SAO" # sem empresas br
simbolo = "AMZN"
url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={simbolo}&apikey={chave_api}'
r = requests.get(url)

data = r.json()

print(data)

import pprint as pt

pt.pprint(data)

resultado = pd.DataFrame(data['annualEarnings'])
display(resultado)