import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_outliers_removed.csv')

print(df.head())

# mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}') # aparece só os 3 primeiros e 2 ultimos digitos, o resto fica ***

# corrigindo datas
df['data'] = pd.to_datetime(df['data'], format= '%Y-%m-%d', errors= 'coerce')

data_atual = pd.to_datetime('today') # vai colocar a data atual como o dia de hoje
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01')) # atualizar a data, "onde a data for menor ou igual a data atual vai atualizar a data para 01-01-1900"
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year # arrumar a idade para ficar de acordo com o ano
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int) # faz basicamente um true or false, condicional
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan # np é numpy, vai atribuir um valor nulo com o .nan

# corrigir campos com multiplas informaçoes
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip()) 
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split(' / ')) > 1 else 'Desconhecido')

# verificando a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço Inválido' if len(x) > 50 or len(x) < 5 else x)

# corrigir dados errados
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido') 

estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'Desconhecido')

print('Dados tratados: \n', df.head())