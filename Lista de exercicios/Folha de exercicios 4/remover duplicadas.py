#! python

quantidade = int(input('Digite a quatidade de valores: '))

lista_valores = []
contador = 1

while contador <= quantidade:
    entrada = input(f'Digite a {contador} entrada: ')
    lista_valores.append(entrada)
    contador += 1

for itens in lista_valores:
    if itens in lista_valores:
        lista_valores.remove(itens)

print(lista_valores)