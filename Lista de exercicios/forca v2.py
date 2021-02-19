#! pyhton

def is_forca(palavra):
    if "*" in palavra:
        return True
    return False

# Etapa 1

import sys

palavra = input("Digite a palavra a ser descoberta pelo jogador: ")

forca = list(palavra)

forca_fechada = list('*' * len(forca))

# Etapa 2
chances = 5
for tentativa, contador in enumerate(range(0, chances)):

    palpite = input("Jogador, digite seu palpite: ")

    for i, letra in enumerate(forca):
        if palpite == letra:
            forca_fechada[i] = letra
            chances -= 1
            print(forca_fechada)

if is_forca(forca_fechada):
    print("Perdeu!")
else:
    print("Ganhou!")