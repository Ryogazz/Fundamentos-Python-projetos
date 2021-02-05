#! python

numero1 = float(input('Digite o valor 1: '))
numero2 = float(input('Digite o valor 2: '))
numero3 = float(input('Digite o valor 3: '))

if numero1 > numero2 and numero2 > numero3:
    print(f'{numero1} {numero2} {numero3}')
elif numero2 > numero1 and numero1 > numero3:
    print(f'{numero2} {numero1} {numero3}')
else:
    print(f'{numero3} {numero2} {numero1}')