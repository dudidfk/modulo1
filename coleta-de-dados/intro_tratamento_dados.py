import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/Projetos programação/clientes.csv')

print(df.head().to_string())
print(df.tail().to_string())

print('Quantidade: ', df.shape)
print('Tipagem: \n', df.dtypes)
print('Valores nulos: \n', df.isnull().sum())
