print('Bem-vindo a minha calculadora!')

while True:

    resultado = None
    num1 = float(input('Escreva o primeiro número: '))
    num2 = float(input('Escreva o segundo número: '))

    operacao = input('Digite a operação (+, -, *, /): ')
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
        if num2 == 0:
            print('Operação Inválida, tente novamente!')
            continue
        else: num1 / num2
    else: 
        print('Operação Inválida!')
        continue
    
    if resultado != None:
        print(f'{num1} {operacao} {num2} = {resultado}')
    continuar = input('Deseja realizar outra operação? (s/n): ')
    if continuar == 'n':
        break

    