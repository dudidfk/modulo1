import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/Projetos programação/modulo1/coleta-de-dados/preparação de dados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial: ')
print(df.info())

