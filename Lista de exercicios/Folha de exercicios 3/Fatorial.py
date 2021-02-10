#! python

n = int(input('Digite o valor: '))
fat = 1
i = 2

while i <= n:
    fat = fat * i
    i = i + 1
    print(f'{fat}')

print(f'O valor de {n} em fatorial e = {fat}')