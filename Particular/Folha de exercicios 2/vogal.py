#! python

letra = input("Digite a letra: ")

if letra in ['a', 'e', 'i', 'o', 'u']:
    print(f'A letra {letra} e uma vogal')
else:
    print(f'A letra {letra} e uma consoante')