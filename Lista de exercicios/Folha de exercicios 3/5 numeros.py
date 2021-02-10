#! python

maior = None
menor = None
soma = 0
media = 0

for contador in range(5):
    n = int(input('Informe um inteiro: '))
    if contador == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

    soma += n
media = int(soma / 5)

print(f'A soma dos numeros digitados e: {soma}')
print(f'A media dos numeros digitados e: {media}')
print(f'O maior numero digitado e: {maior} ')
print(f'O menor numero digitado e: {menor}')