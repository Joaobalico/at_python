# Exercício 01
"""
Calcule a soma de todos os números pares de 1 a N, onde N é um número informado pelo usuário.

Exemplo de execução:
Digite um número: 10
A soma dos números pares de 1 a 10 é: 30
"""

# Pedindo entrada do usuario
num = int(input("Digite um número: "))

# Calculando a soma dos número pares
count = 0
total = 0
while count <= num:
    if count % 2 == 0:
        total = total + count  
    count += 1

# Imprimindo na tela o total
print(total)