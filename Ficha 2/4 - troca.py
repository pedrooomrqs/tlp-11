"""
    @pedro.reis
"""

print("== TROCA DE NUMEROS REAIS ENTRE DUAS VARIAVEIS ==\n")

num1 = float(input("Variavel A >> "))
num2 = float(input("\nVariavel B >> "))

temp = num1
num1 = num2
num2 = temp

print("\nVariavel A =", num1, "; Variavel B =", num2)

print("\nPrima ENTER para terminar...")
input()