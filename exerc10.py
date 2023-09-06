dívida = float(input("Digite o valor inicial da divida: "))
jurosmensal = float(input("Agora digite o valor dos juros mensais: "))
valormensal = float(input("Por fim, digite o valor que será pago mensalmente: "))
mes = 1

if (dívida * (jurosmensal/100) > valormensal):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    jurospago = 0
    while saldo > valormensal:
        juros = saldo * jurosmensal / 100
        saldo = saldo + juros - valormensal
        jurospago = jurospago + juros
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}.")
        mes = mes + 1
    print(f"Para pagar uma dívida de R${dívida:8.2f}, a {jurosmensal:5.2f} % de juros,")
    print(f"você precisará de {mes - 1} meses, pagando um total de R${jurospago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")


#questão:
#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
#Pergunte também o valor mensal que será pago. Imprima o número de meses para
#que a dívida seja paga, o total pago e o total de juros pago