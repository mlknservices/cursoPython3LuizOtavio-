# Exercícios propostos

"""
1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

print()

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print(f'{num} é par.')
    else: print(f'{num} é impar.')

else: print('O valor informado não é um número inteiro.')

"""
2 - Faça um programa que pergunte a hora ao usuário e, bseando-se no horário descrito, exiba a saudação apropriada.
Ex.: Bom dia entre 0-11, boa tarde entre 12-17 e boa noite entre 18-23.
"""
print()

horario = input('Digite um horário (0-23): ')

print()

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('O horário deve estar entre 0 e 23.')
    else:
        if horario <= 11:
            print('Bom dia.')
        elif horario <= 17:
            print('Boa tarde.')
        else:
            print('Boa noite.')
else:
    print('Por favor digite um horário entre 0 e 23.')

"""
3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto", 
se tiver entre 5 e 6 letras escreva "Seu nome é normal" e se tiver mais que 6 letras escreva "Seu nome é muito grande".
"""
print()

nome = input('Informe seu primeiro nome: ')
qtd_caracteres = len(nome)

print()

if qtd_caracteres <= 4:
    print('Seu nome é curto.')
elif qtd_caracteres <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
