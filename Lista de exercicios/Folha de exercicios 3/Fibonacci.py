#! python

x = 0
y = 0
z = 1
while x < 100:
    print(f'{y}')
    print(f'{z}')
    soma = y + z
    y = soma
    z = soma + z
    x += 1