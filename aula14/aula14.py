"""
Documentação e funções built-in úteis
"""

""" isnumeric / isdigit / isdecimal - São funções que retornam um resultado booleano 
validando se o valor informado é um número e se o mesmo é positivo
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print()

print(num1.isnumeric())
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os números para realizar contas.')

print()

num3 = input('Digite um número: ')
num4 = input('Digite outro número: ')

try:
    num3 = float(num3)
    num4 = float(num4)

    print(num3 * num4)
except:
    print('ERROR')
