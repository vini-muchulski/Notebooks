# -*- coding: utf-8 -*-
"""BackTesting de Carteira com Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GH69Hieg9Y-lACYFFyxm2ZcwGDU6FnK1
"""

!pip install bt

!pip install yfinance

# Commented out IPython magic to ensure Python compatibility.
import bt
import yfinance as yf
import pandas as pd
import matplotlib

matplotlib.style.use("seaborn-darkgrid")
# %matplotlib inline

"""# Funcoes"""

def consulta_bc(codigo_bcb):

    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)

    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)

    df.set_index('data', inplace=True)

    return df

def cdi_acumulado(data_inicio, data_fim):

    cdi = consulta_bc(12)

    cdi_acumulado = (1 + cdi[data_inicio:data_fim] / 100).cumprod()
    cdi_acumulado.iloc[0] = 1

    return cdi_acumulado

inicio = "2018-01-01"
fim = "2023-12-31"

cdi = cdi_acumulado(data_inicio=inicio,data_fim=fim)

ativos = ["BPAC11.SA","ITUB3.SA","VALE3.SA","EGIE3.SA","WEGE3.SA"]

carteira = yf.download(ativos,start=inicio,end=fim)["Adj Close"]

carteira["Renda Fixa"] = cdi
carteira.dropna(inplace=True)

carteira

"""# Backtesting

"""

rebalanceamento = bt.Strategy('rebalanceamento',
                                [bt.algos.RunMonthly(run_on_end_of_period=True),
                                 bt.algos.SelectAll(),
                                 bt.algos.WeighEqually(),
                                 bt.algos.Rebalance()])

buy_hold = bt.Strategy('Buy&Hold',
                            [bt.algos.RunOnce(),
                             bt.algos.SelectAll(),
                             bt.algos.WeighEqually(),
                             bt.algos.Rebalance()])

# Realiza o backtest das duas estratégias
bt1 = bt.Backtest(rebalanceamento, carteira)
bt2 = bt.Backtest(buy_hold, carteira[["BPAC11.SA","ITUB3.SA","VALE3.SA","EGIE3.SA","WEGE3.SA"]])

# Obtém os resultados do backtest
resultados = bt.run(bt1, bt2)

"""# Resultados

"""

resultados.display()

resultados.plot()

resultados.get_transactions()

resultados.get_security_weights()

resultados.plot_security_weights()