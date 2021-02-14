#! python
import random

palavras = ['lua', 'casa', 'carro', 'goku', 'escola', 'celular']
acertos = []
palavra = random.choice(palavras)

contador = 0

for i in range(0, len(palavra)):
    acertos.append('*')

while contador <= 5:
    palpite = input("\nDigite a letra do palpite: ")
    palpite = palpite.lower()

    for i in range(0, len(palavra)):
        if palpite == palavra[i]:
            acertos[i] = palpite

        print(acertos[i], end="")

    for j in range(0, len(palavra)):
        if palpite == '*':
            contador = contador + 1
            print('Não existe essa letra na palavra')


