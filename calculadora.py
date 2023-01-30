from funcalc import *
from time import sleep

print('=-' * 15)
print('\t','CALCULADORA')
print('=-' * 15)
print('''Selecione a opção desejada:
1 - Multiplicação
2 - Divisão
3 - Soma
4 - Subtração
5 - Porcentagem
0 - SAIR''')

opção = int(input('Digite a opção desejada: '))
while True:
    if opção == 1:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(multiplicacao(n1, n2))
        continuar = str(input('Deseja fazer nova operação? [S/N] ')).upper().strip()
        if continuar == 'S':
            opção = int(input('Digite a opção desejada: '))
        else:
            print('ENCERRANDO... APLICATIVO')
            sleep(2)
            print('APLICATIVO ENCERRADO')
            break
    elif opção == 2:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(divisao(n1, n2))
        continuar = str(input('Deseja fazer nova operação? [S/N] ')).upper().strip()
        if continuar == 'S':
            opção = int(input('Digite a opção desejada: '))
        else:
            print('ENCERRANDO... APLICATIVO')
            sleep(2)
            print('APLICATIVO ENCERRADO')
            break
    elif opção == 3:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(soma(n1, n2))
        continuar = str(input('Deseja fazer nova operação? [S/N] ')).upper().strip()
        if continuar == 'S':
            opção = int(input('Digite a opção desejada: '))
        else:
            print('ENCERRANDO... APLICATIVO')
            sleep(2)
            print('APLICATIVO ENCERRADO')
            break
    elif opção == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(subtracao(n1, n2))
        continuar = str(input('Deseja fazer nova operação? [S/N] ')).upper().strip()
        if continuar == 'S':
            opção = int(input('Digite a opção desejada: '))
        else:
            print('ENCERRANDO... APLICATIVO')
            sleep(2)
            print('APLICATIVO ENCERRADO')
            break
    elif opção == 5:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print(porcentagem(n1, n2))
        continuar = str(input('Deseja fazer nova operação? [S/N] ')).upper().strip()
        if continuar == 'S':
            opção = int(input('Digite a opção desejada: '))
        else:
            print('ENCERRANDO... APLICATIVO')
            sleep(2)
            print('APLICATIVO ENCERRADO')
            break
    elif opção == 0:
        print('ENCERRANDO... APLICATIVO')
        sleep(2)
        print('APLICATIVO ENCERRADO')
        break