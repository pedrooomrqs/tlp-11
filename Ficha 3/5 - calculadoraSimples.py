"""
    Calculadora Simples
    @pedro.reis     29.set.25
"""

import math

# TITULO DO PROGRAMA
print("== CALCULADORA SIMPLES ==")
print("Programador: Pedro Reis\n")

# ENTRADA DE DADOS
print("****")
print("MENU")
print("****")
print("[+] Soma")
print("[-] Subtração")
print("[*] Multiplicação")
print("[/] Divisão")
print("[P|p] Potênciação\n")

num1 = float(input("Numero 1 >> "))
num2 = float(input("Numero 2 >> "))
opcao = input("\nEscolha a opção pelo caracter indicado --> ")

# PROCESSAMENTO DE DADOS
match opcao:

    case"+":
        print(f"\n{num1} + {num2} = {num1+num2}")

    case"-":
        print(f"\n{num1} - {num2} = {num1-num2}")

    case"*":
        print(f"\n{num1} x {num2} = {num1*num2}")

    case"/":
        print(f"\n{num1} / {num2} = {num1/num2}")

    case"P" | "p":
        print(f"\n{num1} ^ {num2} = {num1^num2}")

    case _:
        print("\nERRO! Opção incorreta.")

# FINALIZAÇÃO
print("\nFim do programa.")
input("Prima ENTER para terminar...")