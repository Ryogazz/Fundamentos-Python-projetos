#! python

def soma(lista):
    soma = 0
    produto = 1
    for item in lista:
        soma = soma + item
        produto = produto * item
    return print(f'O resultado e {soma} \nO produto e {produto}')

list = []

n = int(input('Informe os valores da lista: '))
for i in range(n):
    valor = int(input(f'Informe o {i + 1} valor: '))
    list.append(valor)

print(soma(list))
