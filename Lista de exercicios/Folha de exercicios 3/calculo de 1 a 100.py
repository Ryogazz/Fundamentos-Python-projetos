#! python

soma = 0
for x in range(1, 101):
    soma += x
    if (x % 10 == 0):
        print(f'Valor parcial da soma, somando ate {x}: {soma}')
print('***************************************')
print(f'Valor total da soma: {soma}')
