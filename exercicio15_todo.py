# Exercício 15
"""
Faça um código para validar se um determinado cpf é válido. 
O cpf deve ser informado no formato ddd.ddd.ddd-dd (onde d é um dígito de 0 a 9). 
Para validar o cpf, você deve seguir os seguintes passos:

A validação do CPF (Cadastro de Pessoas Físicas) é um processo que verifica se um número de CPF é válido ou não. O CPF é composto por 11 dígitos e possui um algoritmo específico para validação.

O algoritmo de validação do CPF é baseado em cálculos matemáticos que envolvem os dígitos do número. Aqui está uma descrição passo a passo de como é feita a validação do CPF:

1. Primeiro, é importante remover os caracteres especiais (como pontos e traços) do número do CPF, mantendo apenas os dígitos.
2. Em seguida, é necessário separar os 9 primeiros dígitos do CPF, que são os dígitos base para o cálculo dos dígitos verificadores.
3. Para calcular o primeiro dígito verificador, multiplicamos cada um dos 9 dígitos pela sequência decrescente de números de 10 a 2. Somamos os resultados dessas multiplicações.
4. O resultado da soma é dividido por 11. O dígito verificador é o resto da divisão. Se o resto for igual a 0 ou 1, o dígito verificador é 0. Caso contrário, subtraímos o resto de 11 para obter o dígito verificador.
5. Repetimos o mesmo processo para calcular o segundo dígito verificador, mas agora utilizamos os 9 dígitos do CPF original mais o primeiro dígito verificador calculado no passo anterior multiplicando agora esses dígitos pela sequência decrescente de 11 a 2.
6. Após calcular o segundo dígito verificador, temos o CPF completo com os 11 dígitos.
7. Para validar o CPF, comparamos os dígitos verificadores calculados com os dois últimos dígitos do CPF original. Se forem iguais, o CPF é considerado válido. Caso contrário, o CPF é considerado inválido.

Veja um exemplo em: https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
"""
# cpf = "529.982.247-25"
# cpf = "123.456.789-12" # invalido
# cpf = "777.777.777-77" # invalido

# Pedindo input do usuario
cpf = input("Insira um CPF: ")

# Verificando se o CPF é válido
if "." and "-" in cpf:
    # Removendo pontos e traços
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")
    if cpf.isdigit() and len(cpf) == 11:
      primeiros_nove = cpf[:9]

      # Verifica se todos os dígitos são iguais
      if len(set(cpf)) == 1:
        print("CPF Inválido")
        exit()
        
      # primeira verificacao
      soma = 0
      lista_1_verificacao= [10, 9, 8, 7, 6, 5, 4, 3, 2]
      for i in range(len(primeiros_nove)):
        soma += (int(primeiros_nove[i]) * lista_1_verificacao[i])

      primeiro_digito = (soma * 10) % 11
      if primeiro_digito == 1:
        primeiro_digito = 0
      elif primeiro_digito > 9:
        print("CPF Inválido")
        exit()

      # segunda verificacao
      soma2 = 0
      lista_2_verificacao= [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
      primeiros_dez = primeiros_nove + str(primeiro_digito)
      for i in range(len(primeiros_dez)):
        soma2 += (int(primeiros_dez[i]) * lista_2_verificacao[i])
      segundo_digito = (soma2 * 10) % 11

      # checando se os digitos verificadores sao iguais
      if primeiro_digito == int(cpf[-2]) and segundo_digito == int(cpf[-1]):
        print("CPF Válido")
      else:
        print("CPF Inválido")
    else:    
        print("CPF Inválido")
else:    
    print("CPF Inválido")

#done