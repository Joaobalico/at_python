# Exercício 07
"""
Um investidor tem um capital de R$ 1000,00 para investir em renda fixa.
Atualmente, ele tem duas opções de investimento:
- Poupança: rende 0.5% ao mês
- LCA: rende 0.7% ao mês

Ao final de 10 anos de investimento, quanto o investidor terá ganho a mais se escolher o LCA ao invés da poupança?
"""

# declarando variaveis
num = 1000
poupanca = 0.5
lca = 0.7

# calculando total
total_poupanca = (num * poupanca) * 12 * 10
total_lca = (num * lca) * 12 * 10

# calculando diferença e imprimindo na tela
diferenca = total_lca - total_poupanca
print(diferenca)

#done