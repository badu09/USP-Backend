def soma():
  print(40+2)
soma()

# a função abaixo recebe 2 argumentos
def soma_com_argumentos(a, b):
  print(a + b)

# abaixo é chamado a função para que ela seja executada
soma_com_argumentos(40, 2)

def soma_com_argumentos_e_retorno(a, b):
  return a + b

resposta = soma_com_argumentos_e_retorno(55, 4)
print(resposta)