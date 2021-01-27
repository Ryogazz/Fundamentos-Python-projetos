import sys


def erro():
    print("Erro \nEntrada não suportada\nFavor digitar somente numeros")


nota = float(input("Informe a nota do aluno: "))

def Verificar(nota):
    try:
        float(nota)
        return True
    except ValueError:
        return False



if not nota.isnumeric: 
    erro()
else:
    if nota >= 9:
        print("Quadro de Honra")
    elif nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    elif nota >= 3:
        print("Recuperação + Trabalho")
    else:
        print("Reprovado")
