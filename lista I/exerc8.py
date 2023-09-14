primeirastring = input("Digite a primeira string:")
segundastring = input("Digite a segunda string:")
terceirastring = ""

for letra in primeirastring:
     if letra in segundastring and letra not in terceirastring:
         terceirastring += letra

if terceirastring == "":
    print("caracteres comuns não encontrados.")
else:
    print(f"caracteres em comum: {terceirastring}")

    #questão
   #Escreva um programa que leia duas strings e gere uma terceira com os
# caracteres comuns às duas strings lidas.


