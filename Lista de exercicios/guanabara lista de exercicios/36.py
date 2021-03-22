#! python

Vcasa = float(input('Digite o valor da casa: '))
Vsalario = float(input('Digite o valor do salario: '))
Anos = int(input("Digite em quantos anos vai pagar: "))

def aprovaçao(imovel,salario,tempo):
    meses = tempo * 12
    Vpretacao = imovel / meses
    Psalario = (30 / 100) * salario
    print(f'O valor das prestaçoes seria de {Vpretacao}')
    if Vpretacao > Psalario:
        print('Emprestimo negado')
    else:
        print('Emprestimo aprovado')

if __name__ == "__main__":
    aprovaçao(Vcasa,Vsalario,Anos)