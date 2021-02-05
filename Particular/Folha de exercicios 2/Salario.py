#! python

salario = float(input('Digite o valor do seu salario R$: '))

if salario <= 1000.00:
   salario = ((salario * 30) / 100) + salario
elif salario <= 2000.00:
    salario = ((salario * 25) / 100) + salario
elif salario <= 3000.00:
    salario = ((salario * 20) / 100) + salario
elif salario <= 4000.00:
    salario = ((salario * 15) / 100) + salario
else:
    salario = ((salario * 10) / 100) + salario

print(f'O seu novo salario com reajuste e R$: {salario}')