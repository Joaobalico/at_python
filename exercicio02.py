# Exercício 02
"""
Crie uma lista com números que o usuário informar até que ele digite 'q'.
Exiba a soma dos números informados, a média e o desvio-padrão.
Não utilize bibliotecas ou funções para o cálculo da soma, média e desvio padrão.

Exemplo de execução:
Digite um número (q para sair): 5
Digite um número (q para sair): 10
Digite um número (q para sair): -3
Digite um número (q para sair): q
A soma dos números informados é: 12
A média dos números informados é: 4
O desvio-padrão dos números informados é: 6.5574

No moodle, é possível ver a fórmula para cálculo do desvio padrão.
Veja um exemplo em: https://pt.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
"""

# criando uma lista para armazenar os valores
lista_de_numeros = []

# pedindo entrada do usuario até que ele digite "q"
while True:
    numero = input("Digite um número (q para sair): ")
    lista_de_numeros.append(numero)
    if numero == "q":
        # fazendo a soma
        soma = 0
        for num in lista_de_numeros[:-1]:
          print(num)
          soma += int(num)

        # Cálculo da média
        media = soma / len(lista_de_numeros[:-1])

        # Cálculo do desvio padrão
        soma_quadrados_diferencas = 0
        for num in lista_de_numeros[:-1]:
            diferenca = int(num) - media
            soma_quadrados_diferencas += diferenca ** 2
  
        desvio_padrao = (soma_quadrados_diferencas / len(lista_de_numeros[:-1])) ** 0.5

        # imprimindo o resultado na tela
        print(f"A soma dos números informados é: {soma}")
        print(f"A média dos números informados é: {media}")
        print(f"O desvio-padrão dos números informados é: {desvio_padrao}")
        break