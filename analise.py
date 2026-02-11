
# import numpy as np
# # import matplotlib.pyplot as plt
# # import seaborn
# # import plotly


import pandas as pd
import random

# ideia é ciar 20 'pedidos'

produtos = ['Computador' , 'Monitor' , 'Mouse' , 'Caixa de Som ', 'Teclado','Fone' ]

dados = {
'Produto': [random.choice(produtos) for _ in range(20)],
'Preço': [random.randint(100, 5000) for _ in range(20)],
'Qtd': [random.randint(1, 10) for _ in range(20)]
}

# data frame

df = pd.DataFrame(dados)
# head()-- mostra 'n' pimeiras linas 
# tail() -- mostra 'n' uktimas linas 
# padrao -- 5 linhas 

print(df.head())

print(df.info())

print(30*'-')

print(df.describe()) # analise de estatisticas das colunas 
print(30*'-')
print(30*'-')

print(df.shape)

print(df.columns) # imprimir o nome das colunas 


# imprimir 1 coluna

print(df['Produto'])

# imprimir 2 ou mais colunas
print(df[['Produto','Preço']])

# filtrar o dataframe

df_filtrado = df[df['Qtd']>5] 
print(df_filtrado)

print(30*'-')
print('Multiplicaçao vetorial')

# criar coluna 
# toda conta dentro df é uma operaçao vetorial -- sempre lincando posiçoes 

df['Preço_Final'] = df['Preço'] * df['Qtd']

print(df.head())

# da o nome da coluna e o tipo dela
print(df .dtypes)

df.to_csv('base_criada.csv',index=False)



