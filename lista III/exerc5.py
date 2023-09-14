valordacasa = float(input("digite o valor da casa a comprar:"))
salario = float(input('digite o seu salário:'))
anospagar = int(input('digite os anos a pagar a casa: '))

#valor da prestação : valorcasa/mesesapagar
mesespagar = anospagar * 12 # como pede em anos precisa transformar
prestacao = valordacasa/mesespagar

#prestação mensal não pode ser superior a 30 porcento do salario
prestacaomensal = salario * 0.3 #30/100

if prestacao <= prestacaomensal :
    print(f'parabéns,o valor das prestações é de {prestacaomensal} ')
else:
    print('procure outra casa, tente novamente')

#questão:
#Escreva um programa para aprovar o empréstimo bancário para compra de uma
#casa. O programa deve perguntar o valor da casa a comprar, o salário e a
#quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a
#30% do salário. Calcule o valor da prestação como sendo o valor da casa a
#comprar dividido pelo número de meses a pagar.