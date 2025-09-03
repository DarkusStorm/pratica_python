# Crie um programa que:
# 1. Leia 5 números e armazene-os em uma lista;
# 2. Mostre a lista completa;
# 3. Mostre apenas os números pares da lista;
# 4. Mostre o maior e o menor número.

print("Programa de organização de cinco números.")

numeros = []
for i in range(5):
    num = int(input(f"Insira o {i+1}º número: "))
    numeros.append(num)

pares = []
for num in numeros: # Para cada "num" na lista "números", verifica a condição a seguir;
    if num % 2 == 0: # Verifica se cada "n" presente na lista comparativa possui "0" como resto quando dividido por 2 (todos os números pares não possuem resto ao serem divididos por 2);
        pares.append(num) # Todos os que forem pares (não possuem resto ao serem divididos por 2) são colocados na lista "pares".

print("\nOs números inseridos eram", end=" "), print(*numeros, sep=", ", end=".\n")
print("Os números pares entre os inseridos são", end=" "), print(*pares, sep=", ", end=".\n")
print(f"O menor número entre os inseridos foi {min(numeros)}.")
print(f"O maior número entre os inseridos foi {max(numeros)}.")