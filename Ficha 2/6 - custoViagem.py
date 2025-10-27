
"""
    Calculadora do Custo de uma Viagem
    @pedro.reis         22.set.2025
"""
#TITULO DO PROGRAMA
print("== CALCULADORA DO CUSTO DE UMA VIAGEM ==")
print("Programador: Pedro Reis\n")

#ENTRADA DE DADOS
gasto = float(input("Quanta gasolina gastaste na viagem (l/100 KM) >> "))
distancia = float(input("Quantos KM fizeste na viagem >> "))
preco = float(input("Custo do combustivel (Euros) >> "))

#PROCESSAMENTO DE DADOS
totalGasto = distancia * gasto /100
custoFinal = preco * totalGasto

#SAÍDA DE DADOS
print("\n----------------------------------------------------\n")
print(f"Litros de combustivel gastos: {totalGasto}\n")
print(f"Custo da viagem: {custoFinal}\n")
print("----------------------------------------------------")

#FINALIZAÇÃO
input("\nPrima ENTER para terminar...")