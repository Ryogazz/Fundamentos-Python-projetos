#! python

votos = []
verificar = True

try:
    for i in range(5):
        entrada = int(input(f'Digite a quantidade de votos da chapa {i + 1}  '))
        votos.append(entrada)

except:
    print('Digite somente numeros inteiros')


    totalDeVotos = sum(votos)

def percentual(chapa):
    percentual = (chapa * 100) / totalDeVotos
    return percentual

def resultado(votos,percentual):
   for i in votos:
        if percentual(i) <= 50:

            votos.sort()

            Plugar = votos[4]
            Slugar = votos[3]

            resultado = print(f'haverá segundo turno entre : \n'
                              f'A chapa {votos.index(Plugar) + 1} com {votos[4]} votos \n'
                              f'A chapa {votos.index(Slugar) + 1} com {votos[3]} votos')

        elif percentual(i) > 50:
             votos.sort()
             vencedor = votos[4]
             resultado = print(f'**************************************************************************\n'
                              f'O vencendor foi a a chapa {votos.index(vencedor) + 1} com {votos[4]} votos')

        return resultado


print(resultado(votos,percentual))

print('**************************************************************************')
for i in range(5):
    print(f'A chapa {i +1} recebeu {percentual(votos[i]): .2f} % dos votos, com um total de {votos[i]} votos')
