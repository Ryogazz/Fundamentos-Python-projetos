#! python

lista1 = [1, 3, 20, 50, 33, 99]
lista2 = [99, 20, 3, 0, 77, 2]

contador = 0

for item in lista1:
    if item in lista2:
        print(item, end=" ")
        contador += 1

print(f'\nAs listas possuem {contador} elementos em comum')