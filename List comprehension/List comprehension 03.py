#! python

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)

generator2 = {print(i ** 2) for i in range(10) if i % 2 == 0}

calculadora = [print(f'{i} X {j} = {i * j}') for i in range(1,11) for j in range(1,11)]
calculadora2 = [(f'{i} X {j} = {i * j}') for i in range(1,11) for j in range(1,11)]