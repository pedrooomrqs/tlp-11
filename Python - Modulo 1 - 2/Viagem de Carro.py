"""
    Viagem de Carro
    @pedro.reis     22.set.2025
"""

# Titulo do Programa
print("== CALCULADORA DO CUSTO DE UMA VIAGEM ==")

# Entrada de Dados
customedio = float(input("Consumo médio da viatura (l/100 km) --> "))
distancia = float(input("Distancia a percorrer (km) --> "))
preco = float(input("Preço do litro de combustivel (Euros) --> "))

# Processamento
combgasto = customedio / 100 * distancia
custoviagem = customedio / 100 * distancia * preco

# Saída de Dados
print("Litros de combustivel gastos:", combgasto)
print("Custo da viagem:", custoviagem)

# Finalização
input("Prima <ENTER> para terminar.")