# Exercício 08
"""
Calcule o fatorial de um número informado pelo usuário.
O fatorial de um número n é o produto de todos os inteiros de 1 até n.

Exemplo de execução:
Digite um número: 5
O fatorial de 5 é 120
"""

numero = int(input("Digite um numero: "))

numero_final = 1
for i in range(1, numero):
  numero_final = numero * i
  print(numero_final)
  
print(numero_final)