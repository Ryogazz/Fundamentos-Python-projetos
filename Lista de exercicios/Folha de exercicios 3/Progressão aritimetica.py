#! python

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

dif = n2 - n1

for _ in range(20):
    print(f'{n1} ')
    print(f'{n2}')
    n1 = n2 + dif
    n2 = n1 + dif