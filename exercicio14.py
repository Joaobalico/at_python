# Exercício 14
"""
    Crie um jogo onde o computador escolhe um número aleatório entre 1 e 100 e o usuário tenta adivinhá-lo.
    O programa deve informar se o palpite do usuário é maior ou menor que o número escolhido.

    Exemplo de execução (supondo que o computador escolheu o número 42):

    Computador escolhe um número secreto
    Usuário faz o palpite: 50
    Saída: "Seu palpite é maior que o número escolhido."

    Usuário faz o palpite: 30
    Saída: "Seu palpite é menor que o número escolhido."

    Usuário faz o palpite: 42
    Saída: "Parabéns! Você adivinhou o número!"
"""

import random
numero_pc = random.randint(1, 100)

numero_usuario = int(input("Digite um número: "))

if numero_usuario == numero_pc:
    print("Parabéns! Você adivinhou o número!")
elif numero_usuario < numero_pc:
    print("Seu palpite é menor que o número escolhido.")
else:
    print("Seu palpite é maior que o número escolhido.")