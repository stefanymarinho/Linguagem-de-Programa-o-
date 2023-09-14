mercadoria = float(input("Digite o preço a ser pago pela mercadoria: R$"))
desconto = float(input("Digite o percentual de desconto (%)"))

valordodesconto = (mercadoria * desconto)/ 100
valorcomdesconto = mercadoria - valordodesconto

print("Este é o valor do desconto R$:",valordodesconto)
print("Este é o valor com desconto R$:",valorcomdesconto)


#questão:
#Faça um programa que solicite o preço de uma mercadoria e o percentual de
#desconto. Exiba o valor do desconto e o preço a pagar.