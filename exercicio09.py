# Exercício 09
"""
Adrian, Bruno e Goran queriam se juntar ao clube dos amantes de pássaros. No entanto, eles não sabiam que todos os candidatos devem passar por um exame de admissão. O exame consiste em perguntas, cada uma com três possíveis respostas: A, B e C.

Infelizmente, eles não conseguiam distinguir um pássaro de uma baleia, então estão tentando adivinhar as respostas corretas. Cada um dos três garotos tem uma teoria sobre qual conjunto de respostas funcionará melhor:

Adrian afirma que a melhor sequência é: A B C A B C A B C A B C ...

Bruno está convencido de que esta é melhor: B A B C B A B C B A B C B ...

Goran ri deles e usará esta sequência: C C A A B B C C A A B B C C ...

O gabarito do exercício é dado na variável gabarito. 

Escreva um código que diga quanto cada questão cada um dos garotos acertou. Seu código deve conter comentários.
"""

gabarito = "BBCBCBBCAACABBACCCBCBCABBACBCACBCCBACACCCCABBCCCCABACAABBCAACACBABBACACBBBCABBABCAABCCCBABAAAAABBCBBCABABAAABCCCCACBBBCAABCBCBABCBCBABAACBCCCACAAABCCCCCABBAABACAACCABCBABACBBACCCCCAACBBBCBAACACCACAAAC"

# guardando sequencia de respostas em variaveis
adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

# multiplicando a sequencia para que tenha o tamanho da string gabarito
adrian_sequence = adrian * (len(gabarito) // len(adrian) +1)
bruno_sequence = bruno * (len(gabarito) // len(bruno) +1)
goran_sequence = goran * (len(gabarito) // len(goran) +1)

# inicializando variaveis que vao ser somadas
count_adrian= 0
count_bruno= 0
count_goran= 0

# iterando por cada caractere e verificando as respostas de cada um
for i in range(len(gabarito)):
  if adrian_sequence[i] == gabarito[i]:
    count_adrian += 1
  if bruno_sequence[i] == gabarito[i]:
    count_bruno += 1
  if goran_sequence[i] == gabarito[i]:
    count_goran += 1

# imprimindo na tela os resultados
print(f"Adrian acertou: {count_adrian}")
print(f"Bruno acertou: {count_bruno}")
print(f"Goran acertou: {count_goran}")