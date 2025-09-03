# Crie um programa que faça o seguinte:
# 1. Peça ao usuário que digite seu ano de nascimento;
# 2. Calcule a idade do usuário;
# 3. Classifique o usuário de acordo com a seguinte tabela;
# - Até 12 anos: criança,
# - De 13 a 17 anos: adolescente,
# - De 18 a 64 anos: adulto,
# - De 65 anos para cima: idoso.

# Seção que garante que o programa cheque a data atual automaticamente, sem que seja necessário atualizar o código todos os anos.

import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year

print("Neste programa, usaremos o ano no qual você nasceu para determinar sua idade e em que fase de sua vida você está.")
ano_nascimento = int(input("Insira o ano de seu nascimento: "))

idade = ano_atual - ano_nascimento

if idade <= 12:
    fase_da_vida = "criança"

elif idade >= 13 and idade <= 17:
    fase_da_vida = "adolescente"

elif idade >= 18 and idade <= 65:
    fase_da_vida = "adulto"

elif idade >= 65:
    fase_da_vida = "idoso"

print(f"Sua idade é {idade} e você é {fase_da_vida}.")