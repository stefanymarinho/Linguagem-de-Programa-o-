numero1 = int(input("dividendo:"))
numero2 = int(input("divisor:"))
resultado = 0
i= numero1

while i >=numero2:
    i = i- numero2
resultado = resultado + 1
resto = i
print(f"O resto de {numero1} / {numero2} é {resto}")

#questão:
#Escreva um programa que calcule o resto da divisão inteira entre dois números.
#  Utilize apenas as operações de soma e subtração para calcular o resultado.

