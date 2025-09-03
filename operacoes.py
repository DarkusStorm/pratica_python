# Escreva um programa que;
# 1. Peça ao usuário dois números inteiros.
# 2. Mostre na tela a soma, subtração, multiplicação, divisão, divisão inteira, resto da divisão e exponenciação entre eles.

print("Neste programa, exibiremos diversas operações matemáticas feitas entre dois números inteiros inseridos.")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

soma = n1 + n2
subtracao1 = n1 - n2
subtracao2 = n2 - n1
multiplicacao = n1 * n2
divisao1 = n1 / n2
divisao2 = n2 / n1
divisao_int1 = n1 // n2
divisao_int2 = n2 // n1
resto1 = n1 % n2
resto2 = n2 % n1
potencia1 = n1 ** n2
potencia2 = n2 ** n1

print(f"A soma dos números inseridos é {soma}.")
print(f"A subtração do primeiro número pelo segundo é {subtracao1}, e do segundo pelo primeiro é {subtracao2}.")
print(f"A multiplicação dos números inseridos é {multiplicacao}.")
print(f"A divisão do primeiro número pelo segundo é {divisao1}, e do segundo pelo primeiro é {divisao2}.")
print(f"A divisão inteira do primeiro número pelo segundo é {divisao_int1}, e do segundo pelo primeiro é {divisao_int2}.")
print(f"O resto da divisão do primeiro número pelo segundo é {resto1}, e do segundo pelo primeiro é {resto2}.")
print(f"O primeiro número elevado pelo segundo é {potencia1}, e do segundo pelo primeiro é {potencia2}.")