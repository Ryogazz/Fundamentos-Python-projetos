#! python

def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)


def imposto_importado(importado):
    return 0.22 if importado else 0.13

def imposto_estadual(estadual, multiplicador=1):
    return 0.11 * multiplicador if estadual else 0

if __name__ == '__main__':
    total = calc_preco_final(100, imposto_importado, importado=True)
    total = calc_preco_final(total, imposto_estadual, estadual=True, multiplicador = 2.5)
    print(f'O preço final e R$: {total}')