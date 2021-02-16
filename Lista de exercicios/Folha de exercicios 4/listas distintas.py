#! python

nomes = []
idades = []
sexos = []

def informar_dados(num_pessoas):
  for i in range(num_pessoas):
    nome = input("Informe o nome completo da pessoa: ")
    nomes.append(nome)

    idade = int(input("Informe o idade da pessoa: "))
    idades.append(idade)

    sexo_validade = False
    while(not sexo_validade):
      sexo = input("Informe o sexo da pessoa (M, F ou O): ")
      if(sexo == 'M' or sexo == 'F' or sexo == 'O'):
        if(sexo == 'O'):
          sexo = input("Outro - Informe: ")
        sexos.append(sexo)
        sexo_validade = True
      else:
        print("Valor inválido.")

# Função que calcularia quantas pessoas existem, de um mesmo gênero, na lista sexos
# Use a função .count(), interna do Python, para isso =D
def contar_pessoas_genero(genero):
  contagem = 0
  for sexo in sexos:
    if(sexo == genero):
      # Adicionar +1 à contagem de pessoas daquele gênero
      contagem = contagem + 1
  # Neste ponto, contagem vale o exato número de pessoas daquele gênero
  return contagem

def pessoa_mais_velha():
  pessoa_mais_velha = max(idades)
  # i = índice, na lista de idades, da idade da pessoa mais velha
  i = idades.index(pessoa_mais_velha)
  # na lista de nomes, o nome desta pessoa mais velha também terá índice i
  nome_pessoa_mais_velha = nomes[i]
  print(f"A pessoa mais velha é {nome_pessoa_mais_velha}, que tem {pessoa_mais_velha} ano(s).")

def pessoa_mais_nova():
  pessoa_mais_nova = min(idades)
  i = idades.index(pessoa_mais_nova)
  nome_pessoa_mais_nova = nomes[i]
  print(f"A pessoa mais nova é {nome_pessoa_mais_nova}, que tem {pessoa_mais_nova} ano(s).")

def pessoas_por_genero():
  num_mulheres = sexos.count('F')
  num_homens = sexos.count('M')
  print(f"Existem {num_mulheres} mulher(es) e {num_homens} homem(ns).")

def media_idades(genero):
  soma = 0
  num_pessoas_genero = sexos.count(genero)
  for i in range(num_pessoas):
    if(sexos[i] == genero):
      soma = soma + idades[i]
  media = soma / num_pessoas_genero
  return media

def homem_mais_velho():
  mais_velho = -1
  nome_mais_velho = ''
  for i in range(num_pessoas):
    if(sexos[i] == 'M'):
      if mais_velho == -1:
        mais_velho = idades[i]
        nome_mais_velho = nomes[i]
      elif idades[i] > mais_velho:
        mais_velho = idades[i]
        nome_mais_velho = nomes[i]
  if mais_velho == -1:
    print("Não havia nenhum homem na lista.")
  else:
    print(f"O homem mais velho é {nome_mais_velho}, com {mais_velho} anos(s).")

def mulher_mais_nova():
  mais_nova = -1
  nome_mais_nova = ''
  for i in range(num_pessoas):
    if(sexos[i] == 'F'):
      if mais_nova == -1:
        mais_nova = idades[i]
        nome_mais_nova = nomes[i]
      elif idades[i] < mais_nova:
        mais_nova = idades[i]
        nome_mais_nova = nomes[i]
  if mais_nova == -1:
    print("Não havia nenhuma mulher na lista.")
  else:
    print(f"A mulher mais nova é {nome_mais_nova}, com {mais_nova} ano(s).")


num_pessoas = int(input("Quantas pessoas serão analisadas? "))
informar_dados(num_pessoas)
