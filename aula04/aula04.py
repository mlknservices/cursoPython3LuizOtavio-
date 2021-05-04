"""
* Tipos de dados

str - string = textos 'Assim' ou "Assim"

int - inteiro = 123456 / 0 / -10 / -20 / 1500

float - número real/ponto flutuante = 1.25 / 2.56 / -3.60

bool - booleano/lógico = true/False 10 == 10
"""

print("Marcelo", type("Marcelo"))
print(123, type(123))
print(2.56, type(2.56))
print("L" == "l", type("L" == "l"))

"""
A função " type " exibe o tipo de dado informado
"""

print("10", type("10"), type(int("10")))

"""
Type casting significa transformar o tipo do dado informado, no caso acima o dado foi alterado de "string" para "inteiro".
"""

# Exercício

# Nome: string
print('Marcelo', type('Marcelo'))

# Idade: int
print(42, type(42))

# Altura: float
print(1.98, type(1.98))

# É maior de idade?
print(42 > 18, type(42 > 18))