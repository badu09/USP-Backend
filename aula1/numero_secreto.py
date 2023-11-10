# escolha um número aleatório
# entre 1 e 5
# recebe um chute
# se for igual ao número aleatório => Acertou
# senão, quase, o número secreto era {numero_secreto}

import random

print('\nBem vindo ao Jogo do número secreto! \n\n')

num_secreto = random.randint(1, 5)

chute = int(input('Chute um número entre 1 e 5: \n'))


if chute == num_secreto:
  print('\n Você acertou!! \n')

else:
  print(f'\n Quase... o número secreto é {num_secreto} \n')
