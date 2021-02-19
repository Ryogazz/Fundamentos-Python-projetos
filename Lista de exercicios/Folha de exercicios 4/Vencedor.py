#! python

participantes = []
notas = []

for i in range(10):
    p = input(f'Digite o nome do {i + 1} participante: ')
    n = input(f'Digite a nota do {i + 1} participante: ')
    participantes.append(p)
    notas.append(n)

def vencendor(notas, participantes):
    vencendor = max(notas)
    nome = notas.index(vencendor)
    print(f'o vencedor foi {participantes[nome]} com nota {vencendor}')

print(vencendor(notas, participantes))
