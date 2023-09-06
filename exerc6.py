primeiralista = []
segundalista = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e == 0:
        break
    primeiralista.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e == 0:
        break
    segundalista.append(e)
terceiralista = primeiralista[:]  # Copia os elementos da primeira lista
terceiralista.extend(segundalista)
i = 0
while i < len(terceiralista):
    print(f"{i}: {terceiralista[i]}")
    i = i + 1


#questão:
#Faça um programa que leia duas listas e que gere uma terceira com os elementos
#das duas primeiras