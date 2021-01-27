#! /usr/bin/python3

PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = [
    'joão gosta de futebol e politica',
    'a praia foi legal',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:' , palavra)
            break
else:
    print('Texto autorizado:', texto)    