#! python

salario = float(input('Digite o valor do seu salario: '))
porcentage = float(input('Digite o percentual de reajuste: '))

reajuste = ((salario * porcentage) / 100) + salario

print(f'Seu salario reajustado sera de: {reajuste}')