#! python

def soma_2(a, b):
    return a + b

def soma_3(a, b, c):
    return a + b + c

def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))
    print(soma_n(2,2,2,2,2,2,2,2,2))
    nus = (2,3)
    print(soma_2(*nus))
    nus_2 = (1,1,1,1,1,1,1,1)
    print(soma_n(*nus_2))