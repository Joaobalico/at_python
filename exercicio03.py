# Exercício 03
"""
Escreva um programa que recebe uma lista de números inteiros do usuário.
O programa deve criar uma nova lista contendo apenas os números pares da lista original e imprimi-la.

Exemplo de execução:
Entre com os números separados por espaço: 1 2 3 4 5 6
Números pares: [2, 4, 6]
"""

numeros = "1 2 3 4 5 6"

lista_pares = []
numeros = numeros.replace(" ", "")

for num in numeros:
  if int(num) % 2 == 0:
    lista_pares.append(num)

print(lista_pares)