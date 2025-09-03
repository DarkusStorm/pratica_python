# LAB 3.2.9

# A solução a seguir faz com que a variável palavra exista apenas dentro do "while", e precisa do break para pará-la, visto que não há condição sendo verificada pela estrutura de repetição.
# while True:
#    palavra = input("Insira uma palavra: ").lower()
#    if palavra == "chupacabra":
#        print("Você saiu do loop com sucesso.")
#        break

# A solução a seguir faz com que o while verifique a condição por si só, sem ser necessário o uso de "if". Pelo mesmo motivo, não é necessário o uso de "break".
# palavra = ""
# while palavra != "chupacabra":
#    palavra = input("Insira uma palavra: ").lower()
#        print("Você saiu do loop com sucesso.")

# Mesma coisa da anterior, mas impedindo que o usuário entre em um loop de imediato, e sim apenas se errar.

# palavra = input("Insira uma palavra: ").lower()
# while palavra != "chupacabra":
#    palavra = input("Insira uma palavra: ").lower()
#         print("Você saiu do loop com sucesso.")

# LAB 3.2.10

# palavra = input("Insira uma palavra: ").upper()
# 
# for letra in palavra:
#    if letra == "A":
#        letra = " "
#        continue
#    if letra == "E":
#        letra = " "
#        continue
#    if letra == "I":
#        letra = " "
#        continue
#    if letra == "O":
#        letra = " "
#        continue
#    if letra == "U":
#        letra = " "
#        continue
#    print(letra)

# palavra = input("Insira uma palavra: ").upper()
# for letra in palavra:
#    if letra in "AEIOU":
#        continue

# LAB 3.2.11

# palavra = input("Insira uma palavra: ").upper()
# letras_juntas = ""

# for letra in palavra:
#    if letra in "AEIOU":
#        continue
#    else:
#        letras_juntas += letras_juntas
# print(letras_juntas)

# LAB 3.2.15

etapas = 0
c0 = int(input("Insira um número natural diferente de zero: "))

if c0 < 0:
    int(input("Esse não é um número natural. Insira outro: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        etapas += 1
        print(c0)
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        etapas += 1
        print(c0)

print(f"Etapas = {etapas}")