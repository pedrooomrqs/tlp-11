"""
    Calculadora de Aumento de Vencimento 5% ou 7%
    @pedro.reis         23.set.25
"""

# TITULO DO PROGRAMA
print("== CALCULADORA DE AUMENTO DE VENCIMENTO 5% OU 7% ==")
print("Programador: Pedro Reis\n")

# ENTRADA DE DADOS
vencimento = float(input("Vencimento >> "))

# PROCESSAMENTO DE DADOS
if(vencimento  > 1500  ):
    aumento = vencimento*5/100
    vencimento = vencimento + aumento
    print(f"\nVencimento com aumento de 5% = {vencimento:.2f}€\n")

else:
    aumento = vencimento*7/100
    vencimento = vencimento + aumento
    print(f"\nVencimento com aumento de 7% = {vencimento:.2f}€\n")

if(vencimento < 870 or vencimento > 10000  ):
    print("ERRO! Salario negado\n")

else:
    print("Salario aceite\n")

# FINALIZAÇÃO
print("Fim do programa.")
input("Prima ENTER para terminar...")