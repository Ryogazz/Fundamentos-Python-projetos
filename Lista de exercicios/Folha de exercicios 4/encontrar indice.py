#! python

lista = ['casa', 'carro', 'mesa']


print('itens na lista:')
for i in lista:
    print(f'{i}')


x = input('Digite o nome do item que deseja saber o index: ')

for i in lista:
    if x == i:
        print(f'O indice do item {i} e: ',end = " ")
        print(lista.index(i))
