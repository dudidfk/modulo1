import pandas as pd

df = pd.read_csv('C:/Users/Administrator/Desktop/Projetos programação/modulo1/coleta-de-dados/notas_alunos.csv')


nome = input('Digite seu nome(para sair digite "n"): ')
if nome.lower() == 'n':
    print('Saindo sem adicionar')
    exit()
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

df.loc[len(df)] = {'aluno': nome, 'nota1': nota1, 'nota2': nota2, 'nota3': nota3}

df['media'] = ((df['nota1'] + df['nota2'] + df['nota3']) /3).round(1)
df['status'] = df['media'].apply(lambda x: 'Aprovado!' if x >= 6 else 'Reprovado!')

continuar = input('Deseja adicionar mais algum cadastro? (s/n) ')

df.to_csv('C:/Users/Administrator/Desktop/Projetos programação/modulo1/coleta-de-dados/notas_alunos.csv', index=False)

print(df)