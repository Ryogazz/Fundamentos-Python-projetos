#! python

import random

base_de_dados = 'My Little Pony: A Amizade É Mágica (My Little Pony: Friendship Is Magic na versão original) \
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


base_de_dados = base_de_dados.lower()
verificador = set(base_de_dados)
palavras = base_de_dados.split(' ')

#print(base_de_dados)
#print(verificador)
#print(palavras)


def gerador_de_palavras(base_de_dados):
    print('Entrada:', base_de_dados)

    base_de_dados = base_de_dados.lower()

    print('base_de_dados.lower:', base_de_dados)

    verifcador = set(base_de_dados)

    print('verificador:', verificador)

    palavras = base_de_dados.split(' ')

    print('palavras:', palavras)

    for x in random.shuffle(palavras):
        print('x:', x)

        print('x.isalpha:', x.isalpha())
        print('x>2:', len(x) > 2)
        palavra = x.isalpha() == True and len(x) > 2

        print('palavra:', palavra)

    print('palavra final:', palavra)
    return palavra


gerador_de_palavras(base_de_dados)



