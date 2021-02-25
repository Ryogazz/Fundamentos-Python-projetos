#! python
import random
import sys
import csv
import re
from urllib import request

def base_Dados(url):
    with request.urlopen(url) as texto:
        print('Carregando a base dados')
        texto = texto.read().decode('latin1')
        print('Dowload completo!')
        #palavras = list(map(str, texto.split()))
        palavras = re.compile(r'(?<![.-])\b([a-z]{2,}|[A-Z]{1}[a-z]+|[A-Z]{2,})\b(?!\.|@|\-)').findall(texto)
        palavra = random.choice(palavras)


    return palavra


palavra = base_Dados(r'https://pt.wikipedia.org/wiki/My_Little_Pony:_A_Amizade_%C3%89_M%C3%A1gica')
palavra = palavra.lower()

print(palavra)


acertos = []

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

    if '*' not in acertos:
        print('\nParabens você venceu')
        sys.exit(0)


    if palpite not in palavra:
        chances -= 1
        print('\nNão existe essa letra na palavra')
        print(f'Você tem {chances} chances')

    if chances == 0:
        print('Forca voce perdeu')
        sys.exit(0)
