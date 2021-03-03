#! python
import random
import sys
import csv
import re
from urllib import request

'''def base_Dados(url):
    with request.urlopen(url) as texto:
        print('Carregando a base dados')
        texto = texto.read().decode('latin1')
        print('Dowload completo!')
        #palavras = list(map(str, texto.split()))
        palavras = re.compile(r'(?<![.-])\b([a-z]{2,}|[A-Z]{1}[a-z]+|[A-Z]{2,})\b(?!\.|@|\-)').findall(texto)
        palavra = random.choice(palavras)


    return palavra'''

base_De_Dados = 'My Little Pony: A Amizade É Mágica (My Little Pony: Friendship Is Magic na versão original) \
é uma série de desenho animado de fantasia e infantil para televisão, criada pela Lauren Faust da Hasbro.\
A série é baseado na linha homônima de brinquedos e trabalhos de animação da Hasbro,\
e é frequentemente referido pelos colecionadores como a quarta geração ("G4") da franquia.\
A série estreou nos Estados Unidos, em 10 de outubro de 2010 no extinto The Hub,\
[1] um canal de televisão por assinatura e exibido pela sua sucessão Discovery Family,\
e teve o seu fim realizado no dia 12 de outubro de 2019. A série estreou no Brasil, \
em 21 de novembro de 2011 no Discovery Kids e teve seu fim em 19 de agosto de 2020, \
inacabado sem o seu final faltando dois episódios da nona e última temporada[2], \
e estreou em 17 de dezembro de 2018 na TV Cultura. Em janeiro de 2020 teve sua última \
exibição na grade de programação da Cultura tendo apenas seis temporadas exibidas \
(Exceto as duas partes do final da 6ª temporada), dando lugar a O Diário de Mika no mesmo horário.\
[3] A série estreou em Portugal em 5 de março de 2012 pelo Canal Panda e sendo cancelado até a sua 6ª temporada,\
[4] e também estreou em 17 de outubro de 2016 no JimJam. A série estreou na Angola e Moçambique\
em 3 de fevereiro de 2015 pelo DStv Kids.'

def gerador_de_palavras(base_de_dados):


    base_de_dados = base_de_dados.lower()
    simbolos = ('"', '(', ')', ',', '.', ':', '[', ']')
    for simbolo in simbolos:
        base_de_dados = base_de_dados.replace(simbolo, '')


    verificador = set(base_de_dados)



    palavras = base_de_dados.split(' ')


    random.shuffle(palavras)
    for palavra in palavras:
        if palavra.isalpha() == True and len(palavra) > 2:
            return palavra



#palavra = base_Dados(r'https://pt.wikipedia.org/wiki/My_Little_Pony:_A_Amizade_%C3%89_M%C3%A1gica')
palavra = gerador_de_palavras(base_De_Dados)

print(palavra)


acertos = []

chances = 5
numeroLetra = len(palavra)

for i in range(0, numeroLetra):
    acertos.append('*')


while chances >= 0:
    palpite = input("\nDigite a letra do palpite: ")
    palpite = palpite.lower()
    if len(palpite) > 1:
        print('Digite somente uma letra.')
        continue


    for letra in range(0, numeroLetra):
        if palpite == palavra[letra]:
            acertos[letra] = palpite

        print(acertos[letra], end="")

    if '*' not in acertos:
        print('\nParabens você venceu')
        sys.exit(0)


    if palpite not in palavra:
        chances -= 1
        print('\nNão existe essa letra na palavra')
        print(f'Você tem {chances} chances')

    if chances == 0:
        print('Forca voce perdeu')
        sys.exit(0)
