"""
    Hoje
    @pedro.reis     6.out.2025
"""

print("#####################################################################")
print("CONVERSOR DE MEDIAS DE COMPRIMENTO")
print("POLEGADAS <--> CENTIMETROS")
print("Programador = Pedro Reis")
print("#####################################################################")

print("MENU")

print("#####################################################################")
print("[C] Polegadas --> Centimetros")
print("[P] Centimetros --> Polegadas")
print("[S] Sair")
print("#####################################################################")

opcao = input("Escolha uma opcao: ")

if (opcao == "C" or opcao == "c"):
    valorc = int(input("Digite o valor das polegadas a converter --> "))
    valorp = valorc * 2.54
    print("O valor em centimetros e -->", valorp, "cm")


elif (opcao == "P" or opcao == "p"):
    valorp = int(input("Digite o valor dos centimetros a converter --> "))
    valorc = valorp / 2.54
    print("O valor em polegadas e -->", valorc, "pol")

input("Prima <ENTER> para terminar.")