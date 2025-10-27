"""
    @pedro.reis
"""

print("CALCULADORA DE DESCONTOS")
print("Programador: Pedro Reis")

nome = input(print("\nNome do artigo >> "))
custo = float(input("\nValor do artigo >> "))
percentagem = int(input("\nPercentagem de Desconto >> "))

desconto = custo*percentagem/100

print("\n Artigo:", nome, "|| Valor do Desconto:", desconto, "Euros || Total a pagar:", custo - desconto)