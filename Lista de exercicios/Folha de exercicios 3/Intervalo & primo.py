#! python

n1 = int(input('Digite o inicio do intervalo: '))
n2 = int(input('Digite o final do intervalo: '))

for x in range(n1, n2 + 1):
    cont = 0
    for y in range(n1, x + 1):
        if x % y == 0:
            cont += 1

    if cont <= 2:
        print(f'{x}')