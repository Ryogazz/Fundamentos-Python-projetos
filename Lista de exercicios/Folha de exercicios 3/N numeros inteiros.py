#! python

soma = 0
media = 0
maior = 0
menor = 0

n = int(input('Digite a quatidade de numeros que quer inserir: '))

for contador in range(n):
    n2 = int(input(f'Digite o {contador+1} valor: '))
    if contador == 0:
        maior = n2
        menor = n2
    elif maior < n2:
        maior = n2
    elif menor > n2:
        menor = n2

    soma += n2

media = int(soma / n)

print(f'O maior valor digitado e: {maior}')
print(f'O menor valor digitado e: {menor}')
print(f'A soma dos valores digitados e: {soma}')
print(f'A media dos valores digitados e: {media}')