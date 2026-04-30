import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/Projetos programação/clientes.csv')

pd.set_option('display.width', None)

# removendo dados
df.drop('pais', axis=1, inplace=True) # axis 1 é ref coluna e axis 0 é ref linha. Inplance já altera o próprio df
df.drop(2, axis=0, inplace=True) # removendo a linha 2

# normalizando campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# convertendo os dados 
df['idade'] = df['idade'].astype(int)

print(df)

# tratar valores nulos
print('Valores nulos. \n', df.isnull().sum())

df_fillna = df.fillna(0) # substituir valores nulos com 0
df_dropna = df.dropna() # remover registro com valores nulos
df_dropna4 = df.dropna(thresh=4) # manter registro com no mínimo 4 valores não nulos
df = df.dropna(subset=['cpf']) # remover registro com cpf nulo

print('Quantidade de registros nulos com fillna: ', df_fillna.isnull().sum().sum())
print('Quantidade de registros nulos com dropna: ', df_dropna.isnull().sum().sum())
print('Quantidade de registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())
print('Quantidade de registros nulos com CPF: ', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # mean faz a media, interessante para não correr o risco de atrapalhar no tratamento de dados

# tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') # coerce se tiver algum erro vai gerar um valor nulo

# tratar valores duplicados
print('Qtd de registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True) # remove as duplicatas que tiverem o mesmo cpf cadastrado
print('Qtd de registros removendo as duplicatas: ', len(df))

print('Dados limpos: \n', df)

# salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo dataframe: \n', pd.read_csv('clientes_limpeza.csv'))