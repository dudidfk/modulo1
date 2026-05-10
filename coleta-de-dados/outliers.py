import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_idade = df[df['idade'] > 100]

print('Filtrando a idade: \n', df_filtro_idade[['nome', 'idade']])

# identificar outliers com zscore, outliers > extremos 8 ou 80
z_scores = stats.zscore(df['idade'].dropna()) # dropna nesse caso não precisa pq ja são dados tratados, mas se não fossem ele iria servir
outliers_z = df[z_scores >= 3]
print('Outliers com z_score: \n', outliers_z)

# filtrar outliers com zscore
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# identificar com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: \n', limite_baixo, limite_alto)

# filtrar outliers com IQR
outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)] # | operador de ou, visualizar outliers, todos
print('Outliers pelo IQR: \n', outliers_iqr)
# OU
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)] # visualizar o que nao é outlier, por isso do sinal trocado

limite_baixo = 1
limite_alto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# filtrar endereços válidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço Inválido' if len(x.split('\n')) < 3 else x)
print('Qtd de registros com Enredeços Inválidos: ', (df['endereco'] == 'Endereço Inválido').sum())

# tratar campos com string
df['nome'] = df['nome'].apply(lambda x: 'Nome Inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd de registros com nomes grandes: ', (df['nome'] == 'Nome Inválido').sum())

print('Dados com Outliers tratados: \n', df)

df.to_csv('clientes_outliers_removed.csv', index=False)

