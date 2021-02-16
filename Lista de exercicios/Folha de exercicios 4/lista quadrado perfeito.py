#! python

import random

numeros = []
contador = 0

for i in range(0, 100):
    aleatorio = random.randint(1, 50)
    numeros.append(aleatorio)



for i in numeros:
    raizQ = int(i ** (1/2))
    if(raizQ ** 2) == i:
        print(f'{i} e quadrado perfeito')
        contador += 1

print(f'temos {contador} numeros que sao quadrados perfeitos')