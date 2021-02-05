#! python

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

def bissexto(ano):
  if ano % 400 == 0:
    return True
  elif ano % 4 == 0 and ano % 100 != 0:
    return True
  else:
    return False

def numero_dias(mes, ano):
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    return 31
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    return 30
  elif mes == 2:
    if bissexto(ano):
      return 29
    else:
      return 28
  else:
    return -1

def validar_data(dia, mes, ano):
  # Se o número de dias que o mês possui for maior que o dia que digitei
  if numero_dias(mes, ano) >= dia and dia > 0:
    return True
  else:
    return False

if validar_data(dia, mes, ano):
  print(f"A data {dia}/{mes}/{ano} é válida.")
else:
  print(f"A data {dia}/{mes}/{ano} *não* é válida.")

