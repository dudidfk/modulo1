print('Bem-vindo a minha calculadora!')

while True:
    resultado = None
    
    print('Digite os números a serem calculados.')

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    operacao = input('Digite a operação (+, -, *, /): ')

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print('Operação Inválida, um número não pode ser dividido por zero!')
            continue
        else:
            resultado = num1 / num2
    else:
        print('Operação inválida!')
        continue

    if resultado != None:
        print(f'{num1} {operacao} {num2} = {resultado}')
    continuar = input('Deseja continuar? (s/n)')
    if continuar == 'n':
        break

