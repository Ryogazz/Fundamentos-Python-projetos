#! /usr/bin/python3
from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    Raio = float(input('informe o raio'))
    area = circulo(Raio)
    print('Área do circulo', area)
