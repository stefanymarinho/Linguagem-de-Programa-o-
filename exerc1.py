numero = int(input("Digite um numero:"))

if numero < 0:
    print("Número inválido.Aceitamos apenas números positivos!")
if numero == 0 or numero ==1:
    print(f"{numero} é um caso especial.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"{numero} não é primo")
    else:
        i = 3
        while(i < numero):
            if numero % i == 0:
                break
            i = i + 2
        if i == numero:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo, poisé divisivel por {i}")

#questão:
# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois
# por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.