"""
    Peso de uma Pessoa em Outro Planeta
    @pedro.reis         29.set.25
"""

import math

# TITULO DO PROGRAMA
print("== PESO DE UMA PESSOA NOUTRO PLANETA ==")
print("Programador: Pedro Reis\n")

# ENTRADA DE DADOS
print("--------------------------------------------------")
print("PLANETAS QUE PODEM SER ANALIZADOS -")
print("--------------------------------------------------\n")

print("--------------------------------------------------")
print("[1] Mercurio")
print("[2] Vénus")
print("[3] Marte")
print("[4] Júpiter")
print("[5] Saturno")
print("[6] Urano")
print("--------------------------------------------------\n")

peso = float(input("Seu peso >> "))
planeta = input("\nEscolha o Planeta pelo numero indicado >> ")

# PROCESSAMENTO DE DADOS
match planeta:

    case"1":
        print(f"O seu peso no planeta Mercurio é = {peso*0.37:.2f}kg")

    case"2":
        print(f"O seu peso no planeta Venus é = {peso*0.88:.2f}kg")

    case"3":
        print(f"O seu peso no planeta Marte é = {peso*0.38:.2f}kg")

    case"4":
        print(f"O seu peso no planeta Jupiter é = {peso*2.64:.2f}kg")

    case"5":
        print(f"O seu peso no planeta Saturno é = {peso*1.15:.2f}kg")

    case"6":
        print(f"O seu peso no planeta Urano é = {peso*1.17:.2f}kg")

    case _:
        print("\n ERRO! Planeta invalido.")

# FINALIZAÇÃO
print("\nFim do programa.")
input("Prima ENTER para terminar...")