#! python

numero1 = float(input('Digite o valor 1: '))
numero2 = float(input('Digite o valor 2: '))
numero3 = float(input('Digite o valor 3: '))

if numero1 == numero2 and numero1 == numero3:
    print('Valores iguais')
elif numero1 > numero2 and numero1 > numero3:
    print(f'O valor 1 = {numero1} e maior')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O valor 2 = {numero2} e maior')
else:
    print(f'O valor 3 = {numero3} e maior')