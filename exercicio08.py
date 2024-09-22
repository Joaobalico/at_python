# Exercício 08
"""
Calcule o fatorial de um número informado pelo usuário.
O fatorial de um número n é o produto de todos os inteiros de 1 até n.

Exemplo de execução:
Digite um número: 5
O fatorial de 5 é 120
"""

# pedindo entrada do usuario
numero = int(input("Digite um numero: "))

# multiplicando os valores por cada iteraçao
for i in range(1, numero):
  numero *= i

# imprimindo na tela o resultado pedindo entrada do usuario
print(numero)