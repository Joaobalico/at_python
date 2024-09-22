# Exercício 03
"""
Escreva um programa que recebe uma lista de números inteiros do usuário.
O programa deve criar uma nova lista contendo apenas os números pares da lista original e imprimi-la.

Exemplo de execução:
Entre com os números separados por espaço: 1 2 3 4 5 6
Números pares: [2, 4, 6]
"""

# criando lista para guardar os numeros que o usuario colocar
lista_entrada_usuario = []

# pedindo entrada do usuario até que ele digite "q"
while True:
    numero = input("Digite um número (q para sair): ")
    if numero == "q":
        break
    lista_entrada_usuario.append(numero)


lista_pares = []
# removendo virgulas e parentesis retos da lista
string_entrada_usuario = ' '.join(lista_entrada_usuario)

# verificando se os numeros são pares ou nao
for num in string_entrada_usuario:
  if num == " ":
    continue
  if int(num) % 2 == 0:
    lista_pares.append(num)

print(lista_pares)