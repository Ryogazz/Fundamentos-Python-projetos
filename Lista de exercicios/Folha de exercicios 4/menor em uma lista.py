#! python

def valor(lista):
    maior = lista[0]
    menor = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero

        elif numero < menor:
             menor = numero

    return print(f'O maior valor da lista e {maior} \n'
                 f'O menor valor da lista e {menor}')


list = [10, 4, 8, 27, 100, 32, 55]

print(valor(list))

