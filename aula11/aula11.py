"""
Operadores relacionais

== > >= < <= !=
"""

print(2 == 2)

print()

print(2 == 1)

print()

num_1 = 2
num_2 = '2'

print(num_1 == num_2)

print()

num_3 = 4
num_4 = 5

expressao = (num_3 < num_4)

print(expressao)

print()

var_1 = 'Marcelo'
var_2 = 'MArcondes'

valida = (var_1 != var_2)

print(valida)

print()

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
# Limite para pegar empreéstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
