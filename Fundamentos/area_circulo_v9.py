#! /usr/bin/python3
from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    Raio = sys.argv[1]
    area = circulo(Raio)
    print('Área do circulo', area)
