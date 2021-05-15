"""
Operadores lógicos

and, or, not, in, e not in
"""

a = 2
b = 3
c = 4

var = a == b and b > c

print(var)

print()

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

print()

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

print()

d = ''
e = 20

if not d:  # Está verificando se o valor de "d" foi preenchido, caso negativo a mensagem abaixo será exibida.
    print('Por favor, preencha o valor de "d".')

print()

nome = 'Marcelo'

if 'm' or 'M' in nome:
    print('Existe a letra "m/M" em seu nome.')
else:
    print('Não existe a letra "m/M" em seu nome.')

print()

nome2 = 'Marcelo'

if 'M' not in nome2:
    print('Existe a letra em seu nome.')
else:
    print('Não existe a letra em seu nome.')

print()

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'marcelo'
senha_bd = '123456'

print()

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')
