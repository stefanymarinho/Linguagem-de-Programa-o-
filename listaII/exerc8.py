String = str(input("digite a string:"))

i = {}

for letra in  String :
    i[letra] = i .get(letra,0)+1

for chave, valor in i.items():
    print(f"{chave}: {valor}x")

#questão:
#Escreva um programa que leia uma string e imprima quantas vezes cada caractere
#aparece nessa string. Exemplo: String: BBWWN Resultado: T: 2x B: 2x W: 1N.