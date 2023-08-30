salario = float (input("Digite o salario:"))
percentual = float (input("Digite a porcentagem do aumento:"))

novosalario = salario + ((salario*percentual)/100)
aumento = novosalario - salario

print("salario de R$ " , salario)
print(" Um aumento de  R$  :" , aumento )
print("Novo salário é de: R$" , novosalario)

#questão:
#Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

