#! pyhton

def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__=='__name__':
    todos_params('a','b','c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('pessoa', True,[4,7,10], tamanho="M", fragil=True)