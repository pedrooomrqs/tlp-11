"""
    Antecessor e Succesor de um N.º Inteiro
    @pedro.reis     22.set.2025
"""

# Titulo do Programa
print("== ANTECESSOR E SUCESSOR DE UM N.º INTEIRO ==")

# Entrada de Dados
numero = int(input("Número inteiro: "))

# Processamento
numero_ant = numero - 1
numero_suc = numero + 1

# Saída de Dados
print("Antecessor :", numero_ant, ";", "Sucessor :" ,numero_suc)

# Finalização
input("Prima <ENTER> para terminar.")