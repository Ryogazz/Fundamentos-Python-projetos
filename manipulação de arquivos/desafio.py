#! python

import csv

with open('desafio-ibge.csv') as entrada, open('resposta-desafio.csv', 'w') as saida:
    entrada.readline() #le a primeira linha com isso o for inicia apartir da linha 2 ignorando assim o cabeçalho
    for coluna in entrada:
        cidade = coluna.strip().split(',')
        print(f' {cidade[8]} , {cidade[3]} '.format(*cidade), file=saida)





