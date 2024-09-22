# Exercício 04
"""
Escreva um código que peça um número para o usuário e responda se ele é primo ou não.
Lembrando que um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
Seu código deve conter comentários.
"""

# pedindo entrada do usuario
number = int(input("Digite um número: "))

# verificando se o numero é primo ou nao e imprimindo na tela
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')