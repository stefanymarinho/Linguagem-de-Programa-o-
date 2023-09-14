numero1 = float(input("Primeiro número:"))
numero2 = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = numero1 + numero2
elif operação == "-":
    resultado = numero1 - numero2
elif operação == "*":
    resultado = numero1 * numero2
elif operação == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)


#questão:
#Escreva um programa que leia dois números e que pergunte qual operação você
# deseja realizar. Você deve poder calcular soma (+), subtração (-),
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.