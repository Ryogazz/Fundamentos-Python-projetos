#! /usr/bin/python3

#for i in range(1, 10):
#    if i == 6:
#        break
#    print(i)
#else:
#    print('FIM!')    

from random import randint
def sortear_dado():
    return randint (1, 6)

for i in range(1, 6):
    if i %2 == 1:
        continue
    
    if i == sortear_dado():
        print('ARCERTOU MIZERAVI', i)
        break
else:
    print('Não acertou o numero mizeravi!')
