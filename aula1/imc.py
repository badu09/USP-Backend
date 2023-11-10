print('IMC\n')

# peso / altura * altura

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura: '))

# a função 'round' serve para arredondar o valor final da soma abaixo.
imc = round(peso / altura **2)

print(f'\n O IMC é {imc}')