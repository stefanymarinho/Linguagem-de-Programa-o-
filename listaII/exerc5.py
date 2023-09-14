cigarrospordia = int(input("Quantidade de cigarros por dia:"))
anosfumando = float(input("Quantidade de anos fumando:"))

reduçãoemminutos = anosfumando * 365 * cigarrospordia * 12

reduçãoemdias = reduçãoemminutos / (24 * 60)

print("Redução do tempo de vida %8.2f dias." % reduçãoemdias)

#questão:
#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 12 minutos de vida a cada cigarro, e calcule
#quantos dias de vida um fumante perderá. Exiba o total em dia