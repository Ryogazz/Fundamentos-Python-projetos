#! python

votos = []
verificar = True

def percentual(chapa):
    percentual = (chapa * 100) / totalDeVotos
    return percentual

def resultado(votos,percentual):
    maisVotado = max(votos)
    if percentual(maisVotado) > 50:
        print(f'O vencedor foi a chapa {votos.index(maisVotado) + 1} com {percentual(maisVotado): .2f} % de votos')

    else:
        votos.sort()
        slugar = votos[3]
        print(f'Haverá um segundo turno entre: ')
        print(f'A chapa {votosP.index(maisVotado) + 1} com {percentual(maisVotado): .2f} % de votos')
        print(f'A chapa {votos.index(slugar) +1} com {percentual(slugar): .2f} % de votos')

def resultado_geral(percentual,votos):
    for i in range(5):
       resultadoG = print(f'A chapa {i + 1} recebeu {percentual(votos[i]): .2f} % dos votos, com um total de {votosP[i]} votos')


for i in range(5):
    while True:
        try:
            entrada = int(input(f'Digite a quantidade de votos da chapa {i + 1}  '))
            assert isinstance(entrada,int)
            break
        except:
            print('Erro, digite somente numeros inteiros')

    votos.append(entrada)

votosP = votos.copy()
totalDeVotos = sum(votos)


print(resultado(votos,percentual))
print('**************************************************************************')
print(resultado_geral(percentual, votosP))













