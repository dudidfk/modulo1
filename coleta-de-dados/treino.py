# criar uma lista de notas
# pedir ao usuario quantas notas ele quer adicionar, loop até ele dizer não
# Em cada iteração: leia uma nota (float), adicione à lista
# criar uma função que some as notas e divida pelo tamanho da lista, retornando o resultado
# chamar a funcao e imprimir as notas dizendo se foi aprovado ou não

notas = []

while True:
    entrada = input('Digite uma nota ou (n) para sair: ')
    if entrada == 'n':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print('Digite um número válido!')
        

def calcular_media(lista_notas):
    if len(lista_notas) == 0:
        return 0.0
    return sum(lista_notas) / len(lista_notas)
        

media = calcular_media(notas)
print(f'Média: {media:.1f}')
if media >= 6:
    print(f'Aprovado! Sua média foi {media:.1f}')
else:
    print(f'Reprovado! Sua média foi {media:.1f}')


