# Exercício 05
"""
Escreva um programa que dado o valor de N da variável abaixo calcula o valor da soma:
1 + 1/2 + 1/3 + 1/4 + ... + 1/N

Exemplo de execução:
Se N = 4,
o programa deverá calcular:
1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

Saída esperada:
2.083333333333333
"""

# pedindo entrada do usuario
number = int(input("Digite um número: "))

# declarando a variavel soma e fazendo um loop para somar a cada iteração
soma = 0
for i in range(1, number + 1):
  soma += 1/i

# imprimindo na tela a soma
print(soma)

#done