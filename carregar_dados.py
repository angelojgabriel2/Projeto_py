import pandas as pd

try:
    df = pd.read_csv('base.csv')
    print(df.head())

except Exception as e :
    print(f'Erro ao carregar dados:  {e}')

print(30*'-')
print(df.info())
print(df.dtypes)