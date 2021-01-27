 #! /usr/bin/python3
from math import pi

if __name__ == '__main__':
    Raio = float(input('informe o raio'))
    Area = pi * float(Raio) ** 2
    print("A area do criculo e: {:.2f}".format(Area))

