'''
# LAB 3.2.9

# A solução a seguir faz com que a variável palavra exista apenas dentro do "while", e precisa do break para pará-la, visto que não há condição sendo verificada pela estrutura de repetição.
 while True:
    palavra = input("Insira uma palavra: ").lower()
    if palavra == "chupacabra":
        print("Você saiu do loop com sucesso.")
        break

# A solução a seguir faz com que o while verifique a condição por si só, sem ser necessário o uso de "if". Pelo mesmo motivo, não é necessário o uso de "break".
 palavra = ""
 while palavra != "chupacabra":
    palavra = input("Insira uma palavra: ").lower()
        print("Você saiu do loop com sucesso.")

# Mesma coisa da anterior, mas impedindo que o usuário entre em um loop de imediato, e sim apenas se errar.

 palavra = input("Insira uma palavra: ").lower()
 while palavra != "chupacabra":
    palavra = input("Insira uma palavra: ").lower()
         print("Você saiu do loop com sucesso.")
'''

'''
# LAB 3.2.10

palavra = input("Insira uma palavra: ").upper()
 
for letra in palavra:
    if letra == "A":
        letra = " "
        continue
    if letra == "E":
        letra = " "
        continue
    if letra == "I":
        letra = " "
        continue
    if letra == "O":
        letra = " "
        continue
    if letra == "U":
        letra = " "
        continue
    print(letra)

# Outra solução (ideal)
palavra = input("Insira uma palavra: ").upper()
for letra in palavra:
    if letra in "AEIOU":
        continue
'''

'''
# LAB 3.2.11

palavra = input("Insira uma palavra: ").upper()
letras_juntas = ""

for letra in palavra:
    if letra in "AEIOU":
        continue
    else:
        letras_juntas += letras_juntas
print(letras_juntas)
'''

'''
# LAB 3.2.14

# Solução por Miguel Moreira da Silva

blocos = int(input("Insira o número de blocos: "))  

altura = 0
camada = 1

while blocos >= camada:
    blocos -= camada
    altura += 1
    camada += 1

print("A altura da pirâmide é:", altura)
'''

'''
# LAB 3.2.15

etapas = 0
c0 = int(input("Insira um número natural diferente de zero: "))

if c0 < 0:
    c0 = int(input("Esse não é um número natural. Insira outro: "))

if c0 == 0:
    c0 = int(input("Esse número natural não é diferente de zero. Insira outro: "))

while c0 != 1:
     if c0 % 2 == 0:
          c0 = c0 // 2
          etapas += 1
          print(c0)
     elif c0 % 2 != 0:
          c0 = 3 * c0 + 1
          etapas += 1
          print(c0)

print(f"etapas = {etapas}")
'''

'''
# LAB 3.4.6

lista_chapeu = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no chapéu.

print("Os números que fazem parte da lista são:", *lista_chapeu, end=".\n")

# Etapa 1: escreva uma linha de código que solicita ao usuário que substitua o número do meio por um número inteiro inserido pelo usuário. 

lista_chapeu[2] = int(input("Insira um número inteiro para substituir o terceiro elemento da lista: "))
print("A nova lista é:", *lista_chapeu, end=".\n")

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.

apagar = int(input("Digite 2 se quiser apagar o último elemento da lista: "))
if apagar == 2:
    lista_chapeu.pop()

# Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual.

comprimento = len(lista_chapeu)
print("O tamanho da lista atual é:", comprimento, end=".")
'''

'''
# LAB 3.4.11

beatles = []

print("Etapa 1:", *beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Etapa 2:", end=" "), print(*beatles, sep=", ", end=".\n")

for membro in beatles:
    adicionar = input("Você gostaria de adicionar Stu Sutcliffe e Pete Best à lista? ").lower()
    if adicionar == "sim" or adicionar == "yes":
        beatles.append("Stu Sutcliffe")
        beatles.append("Pete Best")
        print("Etapa 3:", end=" "), print(*beatles, sep=", ", end=".\n")
        print("\nRemovendo-os da lista pela sua saída em 61 e 62...\n")
        del beatles[2:4]
        # ou "beatles.pop" duas vezes.
        print("Etapa 4:", end=" "), print(*beatles, sep=", ", end=".\n")
        continue
    beatles.insert(0, "Ringo Starr")
    print("\nEtapa 5:", end=" "), print(*beatles, sep=", ", end=".\n")
    break

print("The Fab", len(beatles), end="!")
'''

'''
# LAB 3.6.6

lista1 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista2 = lista1[:]

for num in lista1:
    if num == num in lista2: # Lê cada número número da "lista1" e compara-o com os números da "lista2". Se forem iguais, ele o deleta (basicamente verifica se o número está repetido, mas usando a outra lista como parâmetro)
        del [lista1[num]]

lista1.sort()

print("Lista original: ", end=""), print(*lista2, sep=", ", end=".\n")
print("Lista com elementos exclusivos: ", end=""), print(*lista1, sep=", ", end=".")
'''