#! /usr/bin/python3
PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
textos = [
    'joão gosta de futebol e politica',
    'a praia foi legal',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado: ', texto)    