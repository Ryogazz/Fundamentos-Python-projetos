#! python

chapa1 = 30
chapa2 = 27
chapa3 = 42
chapa4 = 70
chapa5 = 92

totalDeVotos = chapa1 + chapa2 + chapa3 + chapa4 + chapa5

def percentual(chapa):
    percentual = (chapa * 100) / totalDeVotos
    return percentual



print(f'A chapa 1 recebeu {percentual(chapa1): .2f} % dos votos com um total de {chapa1} votos')
print(f'A chapa 2 recebeu {percentual(chapa2): .2f} % dos votos com um total de {chapa2} votos')
print(f'A chapa 3 recebeu {percentual(chapa3): .2f} % dos votos com um total de {chapa3} votos')
print(f'A chapa 4 recebeu {percentual(chapa4): .2f} % dos votos com um total de {chapa4} votos')
print(f'A chapa 5 recebeu {percentual(chapa5): .2f} % dos votos com um total de {chapa5} votos')