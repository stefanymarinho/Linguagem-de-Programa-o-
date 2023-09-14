peso= float(input('digite seu peso:'))
altura =float(input('digite sua altura: '))

imc= (peso /( altura * altura))  #kg*m2

if imc < 18.5: #abaixo de 18.5
    print('abaixo do peso')
elif  18.5 <= imc < 24.9: #entre 18.5 e 24.9
    print('peso normal')
elif 25 <= imc < 29.9:
    print('sobrepeso')
elif 30 <= imc <= 34.9:
    print('obesidade grau I')
else:
    print(('obesidade grau II'))

#questão:
#Desenvolva um algoritmo que peça ao usuário que insira seu peso em kg e sua
#altura em metros. Calcule o Índice de Massa Corporal (IMC) e informe em qual
#categoria ele se encaixa (por exemplo: abaixo do peso, peso normal, sobrepeso,
#obesidade grau I ou grau II