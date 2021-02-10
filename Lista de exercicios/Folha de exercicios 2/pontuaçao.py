#! python

distancia = int(input('Digite distancia da bola: '))

if distancia <= 800:
    print('1')
elif distancia <= 1400:
    print('2')
elif distancia <= 2000:
    print('3')
else:
    print('Distancia incorreta!')