"""
    Conversor de Medidas de Comprimento
    @pedro.reis          6.out.25
"""
import os

# FUNÇÕES DO SISTEMA 
def asteriscos():
    for i in range(60):
        print("*", end =" ")
    print()

def polTOcm():
    valorPol = float(input("\nDigite o valor das polegadas a converter >> "))
    valorCen = valorPol * 2.54
    print(f"Conversão em centimetros = {valorCen:.2f}cm")

def centTOpol():
    valorCen = float(input("\nDigite o valor de centímetros a converter >> "))
    valorPol = valorCen / 2.54
    print(f"Conversão em polegadas = {valorPol:.2f}pol")

# PROGRAMA PRINCIPAL
asteriscos()
print("CONVERSOR DE MEDIDAS DE COMPRIMENTO")
print("POLEGADAS <--> CENTIMETROS ")
print("Programador: Pedro Reis")
asteriscos()
print("Menu")
asteriscos()
print("[C] Polegadas --> Centimetros")
print("[P] Centimetros --> Polegadas")
print("[S] Sair")
asteriscos() 

opcao = input("\nPrima a tecla de uma opção válida >> ")

match opcao:
    case 'c' | 'C':
        polTOcm()

    case 'p' | 'P':
        centTOpol()

    case 's' | 'S':
        exit()

    case _:
        print("\nERRO! Opção incorreta.")

# FINALIZAÇÃO
print("\nFim do programa.")
input("Prima ENTER para terminar...")