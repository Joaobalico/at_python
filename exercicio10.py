# Exercício 10
"""
Peça ao usuário para informar um número e exiba a tabuada de multiplicação desse número de 1 a 10.

Exemplo de execução:
Informe um número: 5
A tabuada de 5 é:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

# entrada do usuario
numero = int(input("Digite um número: "))

# declarando variavel para guardar os valores
tabuada= []

# iterando pelo intervalo do numero e multiplicando os valores
print(f"A tabuada de {numero} é:")
for i in range(1,11):
  tabuada.append(numero* i)
  print(f"{numero} x {i} = {tabuada[i-1]}")