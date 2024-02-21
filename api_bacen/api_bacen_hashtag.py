# -*- coding: utf-8 -*-
"""api_bacen_hashtag

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XIwzGK5ZAb1MID0NKVBotqhC7xUjmzv6

#api do bacen
https://dadosabertos.bcb.gov.br/dataset?res_format=API
"""

import requests
import pprint as pr
import pandas as pd

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=100&$orderby=Data%20desc&$format=json"
requisicao = requests.get(link)
infos = requisicao.json()
#pr.pprint(infos)

tabela = pd.DataFrame(infos["value"])

#tabela["Quantidade"] = tabela["Quantidade"].map("{:,.2f}".format)
tabela["Valor"] = tabela["Valor"].map("{:,}".format)

display(tabela)