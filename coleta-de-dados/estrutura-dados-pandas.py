import pandas as pd

# Criando uma lista de dicionários, onde cada dicionário representa uma linha de dados
dados = [
    {"nome": "Alice", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro"},
    {"nome": "Charlie", "idade": 35, "cidade": "Belo Horizonte"},
]

# Criando um DataFrame a partir da lista de dicionários
df = pd.DataFrame(dados)

# Acessando as colunas 'nome' e 'idade', é necessário abrir os colchetes duplos para acessar múltiplas colunas
print(df[['nome', 'idade']])

df['salario'] = [5000, 4500, 6000] # Adicionando uma nova coluna 'salario' ao DataFrame

df.loc[len(df)] = { # Adicionando uma nova linha ao DataFrame usando um dicionário,
    'nome': 'David', # o índice é definido como o comprimento atual do DataFrame para adicionar a nova linha no final
    'idade': 28, 
    'cidade': 'Curitiba', 
    'salario': 5500
}

df.loc[len(df)] = [ # Adicionando uma nova linha ao DataFrame usando uma lista,
    'Eve',          # necessário garantir que a ordem dos valores corresponda à ordem das colunas
    22,
    'Porto Alegre',
    4800
]

df.drop('salario', axis=1, inplace=True) # Removendo a coluna 'salario' do DataFrame, o parâmetro 'inplace=True' garante que a alteração seja feita no próprio DataFrame
print(df)

filtro_idade = df[df['idade'] >= 30] # Criando um filtro para selecionar apenas as linhas onde a idade é maior ou igual a 30
print(filtro_idade)

df.to_csv('dados.csv', index=False) # Exportando o DataFrame para um arquivo CSV, o parâmetro 'index=False' evita que o índice seja incluído no arquivo
# df.to_excel('dados.xlsx', index=False) # Exportando o DataFrame para um arquivo Excel, o parâmetro 'index=False' evita que o índice seja incluído no arquivo

df.lido = pd.read_csv('dados.csv') # Lendo os dados de volta do arquivo CSV para um novo DataFrame  
print(df.lido)