#! python

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / altura**2

print(f'O seu IMC e: {imc}')