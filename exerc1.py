dias = int(input("digite a quantidade de dias: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))

total = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("o valor total em segundos é de %is." %total)



#questão:
#Escreva um programa que leia a quantidade de dias, horas, minutos e
# segundos do usuário. Calcule o total em segundos.

