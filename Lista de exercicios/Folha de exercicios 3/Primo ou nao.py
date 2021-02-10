#! python

n = int(input('Informe o valor:'))
for i in range(2, n + 1):
    if i != n:
        if n % i == 0:
            print('Nao e primo')
            break
    else:
        print('O valor e primo')