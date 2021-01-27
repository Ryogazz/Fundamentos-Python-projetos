#! /usr/bin/python3
from math import pi


def circulo(raio):
    print('A area do circulo e: ', pi * float(raio) ** 2)


if __name__ == '__main__':
    Raio = float(input('informe o raio'))
    circulo(Raio)
