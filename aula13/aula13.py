"""
A funcão "len" retorna a quantidade de caracteres da variável pesquisada, e o tipo desta funcão é "int"
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print()

if qtd_caracteres < 6:
    print('Seu usuário precisa ter pelo menos 6 caracteres.')
else:
    print('Seu usuário foi cadastrado no sistema.')

print()

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
