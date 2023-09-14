n = int(input('digite o numero a se tornar fatorial:'))
c = n
f = 1
print(f'calculando{n}')
while c > 0:
  print(f"{c}")
  print('x' if c > 1 else '=')
  f *= c
  c -= 1
print(f"{f} ")









#questão:
#Escreva um programa que calcule o fatorial de um número usando um loop.
#(Sabendo que o fatorial de um número se trata da multiplicação desse número
#por todos os seus antecessores maiores que zero.)
