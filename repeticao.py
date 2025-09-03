# Crie um programa que solicite um número ao usuário e imprima na tela todos os números de 0 até o número selecionado.

print("Neste programa, será escrito na tela todos os números que antecedem o inserido pelo usuário.")

numero_escolhido = int(input("Insira um número para iniciar: "))

primeiro_numero = 0
while primeiro_numero < numero_escolhido and numero_escolhido != 0:
    print(primeiro_numero)
    primeiro_numero += 1
print(numero_escolhido)
print("Esse é o número selecionado e os que o antecedem.")