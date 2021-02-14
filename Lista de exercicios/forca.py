#! python
import random
import sys

palavras = ['lua', 'casa', 'carro', 'goku', 'escola', 'celular']
acertos = []
palavra = random.choice(palavras)

chances = 5
numeroLetra = len(palavra)

for i in range(0, numeroLetra):
    acertos.append('*')


while chances >= 0:
    palpite = input("\nDigite a letra do palpite: ")
    palpite = palpite.lower()
    if len(palpite) > 1:
        print('Digite somente uma letra.')
        continue


    for letra in range(0, numeroLetra):
        if palpite == palavra[letra]:
            acertos[letra] = palpite

        print(acertos[letra], end="")


    if palpite not in palavra:
        chances -= 1
        print('\nNão existe essa letra na palavra')
        print(f'Você tem {chances} chances')

    if chances == 0:
        print('Forca voce perdeu')
        sys.exit(0)
