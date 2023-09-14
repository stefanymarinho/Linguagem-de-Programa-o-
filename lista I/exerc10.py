while True:
    print("""
    
Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        numero = int(input("Tabuada de:"))
        i = 1
        while i <= 10:
            if opção == 1:
                print(f"{numero} + {i} = {numero + i}")
            elif opção == 2:
                print(f"{numero} - {i} = {numero - i}")
            elif opção == 3:
                print(f"{numero} / {i} = {numero / i:5.4f}")
            elif opção == 4:
                print(f"{numero} x {i} = {numero * i}")
            i = i + 1
    else:
        print("Opção inválida!")

        #questão
#Escreva um programa que exiba uma lista de opções (menu): adição, subtração
# , divisão, multiplicação e sair.
#Imprima a tabuada da operação escolhida.Repita até que a opção saída seja escolhida.