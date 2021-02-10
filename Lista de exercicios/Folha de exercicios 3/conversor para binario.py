#! python

valor = int(input('Informe o valor: '))
resultado = ''

print(f'A conversão de {valor}', end=' ')

while valor != 0:
    resto = valor % 2
    valor = int(valor/2)
    resultado = str(resto) + resultado

print(f'Para binario é: {resultado}.')