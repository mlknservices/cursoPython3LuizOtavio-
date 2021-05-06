"""
* Variáveis

Iniciar com letra, pode conter números, seprar _, letras minúsculas
"""

nome = 'Marcelo'
print(nome, type(nome))

nome = 'Marcelo Marcondes'

idade = 42

altura = 1.98

e_maior = idade > 18

peso = 155

imc = peso / altura ** 2

print('Nome:', nome)

print('Idade:', idade)

print('Altura:', altura)

print('É maior:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)