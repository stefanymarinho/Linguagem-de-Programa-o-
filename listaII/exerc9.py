soma = 0
quantidade = 0

while True:
    numeros = int(input("digite os números  (0 para terminar)"))
    if numeros == 0:
        break
    soma = soma + numeros
    quantidade = quantidade + 1

print("Quantidade de numeros digitados:",quantidade)
print("Soma :",soma)
print(f"Media: {soma/quantidade:10.2f}")

#questão:
#Escreva um programa que leia números inteiros do teclado. O programa deve ler
#os números até que o usuário digite 0 (zero). No final da execução, exiba a
#quantidade de números digitados, assim como a soma e a média aritmética