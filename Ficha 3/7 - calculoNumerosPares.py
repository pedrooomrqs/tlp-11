"""
    Processamento de Numeros Pares
    @pedro.reis         30.set.25
"""
# TITULO DO PROGRAMA
print("== PROCESSAMENTO DE NÚMEROS PARES ==")
print("Programador: Pedro Reis\n")

# ENTRADA DE DADOS
valIni = int(input("Diz-me um Valor inicial >> "))
valFin = int(input("Diz-me um Valor final >> "))

if(valIni > valFin):
    varTemp = 0
    print("\nOs valores serão trocados por causa do valor final ser maior que o inicial.")
    varTemp = valIni
    valIni = valFin
    valFin = varTemp

# PROCESSAMENTO & SAÍDA DE DADOS
contador = 0
soma = 0

print("\nLista de números pares:")
for i in range(valIni, valFin + 1):

    if(i %2 == 0):
        print(i, end = " ")
        contador += 1
        soma += i

print(f"\n\nForam exibidos {contador} números pares")
print(f"Soma = {soma}")

# FINALIZAÇÃO
print("\nFim do programa.")
input("Prima ENTER para terminar...")