#! /usr/bin/python3
from math import pi
import sys
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessario informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor númerico')
        sys.exit(errno.EINVAL)

    Raio = sys.argv[1]
    area = circulo(Raio)
    print('Área do circulo', area)
