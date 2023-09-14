numero = input('digite um numero:')

palindromo = numero[:: -1]

if numero == palindromo:
    print(' É palíndromo')
else:
    print('Não é palíndromo')
#questão:
#Escreva um programa que verifique se um número é palíndromo. (Um número é
#palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos:
#454, 10501)