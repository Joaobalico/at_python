# Exercício 12
"""
Quando eu como meus Skittles, sempre como os vermelhos por último. Eu os separo em grupos de cores e começo comendo os laranjas, depois os azuis, verdes, amarelos, rosas, violetas, marrons e, finalmente, os vermelhos. Os vermelhos são os melhores, então eu os como devagar, um de cada vez. As outras cores eu como rapidamente aos punhados (minha mão pode segurar no máximo 7 Skittles). Eu sempre termino todos os Skittles de uma cor antes de passar para a próxima, então às vezes o último punhado de uma cor não está completamente cheio. Mas espere, tem mais! Eu transformei meu hábito de comer Skittles em uma ciência. Eu sei que sempre levo exatamente 13 segundos para comer um punhado de Skittles que não são vermelhos e ajusto minha taxa de mastigação para que eu sempre leve 13 segundos, mesmo que minha mão não esteja completamente cheia. Quando como os Skittles vermelhos, gosto de levar meu tempo, então levo exatamente 16 segundos para comer cada um. Eu tenho uma grande caixa de Skittles. Depois de terminar de separar as cores, quanto tempo levará para comê-los? 

 Abaixo está uma lista de cores de Skittles em minha caixa. Cada cor é representada por uma string.
"""

saco_de_skittles = [
    "vermelho",
    "marrom",
    "marrom",
    "violeta",
    "azul",
    "rosa",
    "azul",
    "azul",
    "rosa",
    "marrom",
    "amarelo",
    "marrom",
    "rosa",
    "violeta",
    "verde",
    "amarelo",
    "vermelho",
    "laranja",
    "laranja",
    "azul",
    "marrom",
    "rosa",
    "vermelho",
    "vermelho",
    "vermelho",
    "marrom",
    "laranja",
    "laranja",
    "verde",
    "vermelho",
    "laranja",
    "violeta",
    "azul",
    "rosa",
    "amarelo",
    "rosa",
    "marrom",
    "laranja",
    "verde",
    "vermelho",
    "azul",
    "amarelo",
    "verde",
    "laranja",
    "marrom",
    "laranja",
    "rosa",
    "violeta",
    "marrom",
    "vermelho",
]

# 7 Skittles
# 13 segs
# 16 segs vermelho

count=0
for i in saco_de_skittles:
    if i != "vermelho":
      count+= 1

segundos_skittles_vermelho = saco_de_skittles.count("vermelho") * 16
segundos_outras_cores= count * 13
total = (segundos_outras_cores + segundos_skittles_vermelho) / 60

minutos = round(total, 2)
print(f"{int(minutos)} minutos e {str(minutos).split('.')[1]} segundos")

#done