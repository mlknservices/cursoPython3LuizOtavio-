"""
Desafio prático

* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa baseado na idde e no ano atual
* Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Marcelo Marcondes'

idade = 42

altura = 1.98

peso = 154

ano_atual = 2021

ano_nasc = ano_atual - idade

imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} mts de altura e pesa {peso} kg.')

print(f'O IMC de {nome} é {imc:.2f}.')

print(f'{nome} nasceu em {ano_nasc}.')
