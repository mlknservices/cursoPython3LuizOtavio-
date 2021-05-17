"""
Formatando valores com modificadores

:s - Texto (strings)
nu
:d - Inteiros (int)

:f - Números de ponto flutuante (float)

:.(NUMERO)f - Quantidade de casas decimais (float)

:(CARCTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda

< - Direita

^ - Centro
"""

num_1 = 10

num_2 = 3

divisao = num_1 / num_2

print()

print('{:.2f}'.format(divisao))  # Arredondamento para duas casas depois do ponto

print()

print(f'{divisao:.2f}')  # Arredondamento para duas casas depois do ponto

print()

nome= 'Marcelo Marcondes'

print(f'{nome:s}')  # Declarando que a variável "nome" é uma String

print()

num_3 = 1

print()

print(f'{num_3:0>10}')  # Declarando que o valor a ser demonstrado deve conter 10 caracteres completando com zeros a esquerda

print()

num_4 = 1150

print()

print(f'{num_4:0<10}')  # Declarando que o valor a ser demonstrado deve conter 10 caracteres completando com zeros a direita

print()

print(f'{num_4:0>10.2f}')

print()

nome2 = ' Marcelo Marcondes '
print(len(nome))

print(f'{nome2:#^50}')  # Declarando que a variável deve ter 50 carateres com o valor da variável no meio de #

print()

nome_formatado = '{:@>50}'.format(nome2)

print(nome_formatado)

print()

nome3 = 'Marcelo'
sobrenome = 'Marcondes'

nome_indice = '{0:$^15} {1:#^15}'.format(nome3, sobrenome)  # Selecionando a variável de acordo com o índice informado

print(nome_indice)

print()

nome4 = 'Marcelo Marcondes'

nome4 = nome4.ljust(30, '#')  # Justifica no mome a esquerda (left) e preenche com o caracter informado "#" até a quantidade de caracteres informada "30"

print(nome4)

print()

nome5 = 'Marcelo Marcondes'

print(nome5.lower())  # Todas as letras ficarão minúsculas

print()

print(nome5.upper())  # Todas as letras ficarão maísculas

print()

print(nome5.title())  # A primeira letra de todas as palavras será maíscula e as demais minísculas
