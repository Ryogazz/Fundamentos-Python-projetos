#! python

valores = int(input('Digite a quantidade de valores: '))

listaInteiros = []

contador = 1
while contador <= valores:
    valor = int(input(f'Digite o {contador} valor: '))
    listaInteiros.append(valor)
    contador += 1

listaInteiros.reverse()

print(listaInteiros)