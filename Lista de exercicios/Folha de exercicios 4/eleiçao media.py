#! python

votos = []

for i in range(5):
    entrada = int(input(f'Digite a quantidade de votos da chapa {i + 1}  '))
    votos.append(entrada)

totalDeVotos = sum(votos)

def percentual(chapa):
    percentual = (chapa * 100) / totalDeVotos
    return percentual

cont = 0
for i in votos:
    if percentual(i) < 50.00:
        cont += 1

    if cont == 5:
        print('haverá segundo turno entre :')
        votos.sort()

        Plugar = votos[4]
        Slugar = votos[3]

        print(f'A chapa {votos.index(Plugar) + 1} com {votos[4]} votos')
        print(f'A chapa {votos.index(Slugar) + 1} com {votos[3]} votos')

if cont < 5:
   votos.sort()
   vencedor = votos[4]
   print('**************************************************************************')
   print(f'O vencendor foi a a chapa {votos.index(vencedor) + 1} com {votos[4]} votos')



print('**************************************************************************')
for i in range(5):
    print(f'A chapa {i +1} recebeu {percentual(votos[i]): .2f} % dos votos, com um total de {votos[i]} votos')
