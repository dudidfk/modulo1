import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

dados_pessoas = []
# Gerando dados fictícios para 10 pessoas usando a biblioteca Faker, cada pessoa é representada por um dicionário com as chaves 'nome', 'cpf', 'idade', 'endereco', 'estado' e 'pais'
for _ in range(10):
    nome = fake.name()
    cpf = fake.cpf()
    idade = random.randint(18, 80)
    endereco = fake.address()
    estado = fake.state()
    pais = 'Brasil'
    
    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }
    
    dados_pessoas.append(pessoa)
# Criando um DataFrame a partir da lista de dicionários, onde cada dicionário representa uma pessoa com seus dados       
df_pessoas = pd.DataFrame(dados_pessoas)

pd.set_option('display.max_columns', None) # Configura o pandas para exibir todas as colunas do DataFrame
pd.set_option('display.width', None) # Configura o pandas para ajustar a largura de exibição do DataFrame automaticamente
pd.set_option('display.max_rows', None) # Configura o pandas para exibir todas as linhas do DataFrame
pd.set_option('display.max_colwidth', None) # Configura o pandas para exibir o conteúdo completo de cada célula, sem truncamento

print(df_pessoas) # Exibe o DataFrame, mostrando todas as colunas e linhas, mas pode truncar o conteúdo das células se for muito longo
# print(df_pessoas.to_string()) # Exibe o DataFrame completo como uma string, garantindo que todas as colunas e linhas sejam mostradas sem truncamento

df_pessoas.to_csv('dados_pessoas.csv', index=False) # Exporta o DataFrame para um arquivo CSV, o parâmetro 'index=False' evita que o índice seja incluído no arquivo