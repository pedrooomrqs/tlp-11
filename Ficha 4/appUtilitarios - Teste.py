"""
    App de Utilitarios
    @pedro.reis         23.set.25
"""
# IMPORTS
import os
import math
import random

# FUNÇÕES DO SISTEMA
def tracos():
    for i in range(30): # CRIA UMA LINHA DE 30 CARACTERES DE TRAÇOS
        print("-", end =" ")
    print()

def asteriscos():
    for i in range(30): # CRIA UMA LINHA DE 30 CARACTERES DE ASTERISCOS
        print("*", end =" ")
    print()

def menu():
    os.system('cls') # LIMPA O ECRÃ
    tracos()
    print("APP DE UTILITARIOS")
    print("Programador: Pedro Reis")
    tracos()

    print("\nMENU")
    asteriscos()
    print("[1] Raízes de uma equação de 2.º grau")
    print("[2] Jogo da adivinha")
    print("[0] Sair do script")
    asteriscos()

    opcao = input("\nEntre com um a opção pelo número indicado --> ")
    return opcao

# ENTRADA DE DADOS
while True:
    opcaoTOopcao = menu()

# PROCESSAMENTO DE DADOS
    match opcaoTOopcao:
        case "1":
            os.system('cls') # LIMPA O ECRÃ
            tracos()
            print("RAÍZES DE UMA EQUAÇÃO DE 2.º GRAU")
            print("         ax^2 + bx + c = 0")
            print("         Programador: Pedro Reis")
            print("->NÃO FUNCIONAL!!!<-")
            tracos()

            a = float(input("\nA >> "))
            if (a == 0):
                print("ERRO! não é uma equação de 2.º Grau.")
            b = float(input("B >> "))
            if (b < 0):
                print("ERRO! não tem raízes reais.")
            c = float(input("C >> "))

            print(f"\nA equação é do tipo: {a}x^2 + {b}x + {c} = 0")

            input("\nPrima ENTER para voltar ao menu inicial...")

        case "2":
            os.system('cls') # LIMPA O ECRÃ
            randomNum = random.randint(1, 20) # DESIGNA A VARIAVEL 'randomNum' COM UM NUMERO INTEIRO ALEATORIO DE 1 A 20

            tracos()
            print("JOGO DA ADIVINHA")
            print("Adivinhe o número gerado pelo computador")
            print("         Programador: Pedro Reis")
            tracos()

            print("\nO seu computador gerou um número aleatório entre 1 e 20")
            print("\nDispõe de 5 tentativas para adivinhar esse numero:\n")

            for i in range (1, 5 + 1):

                escolha = int(input(f"O seu {i}.º palpite para o número gerado automaticamente >> "))
                if (randomNum > escolha):
                    print("O numero gerado é maior.\n")
                elif (randomNum < escolha):
                    print("O numero gerado é menor.\n")
                elif (escolha == randomNum):
                    print(f"\nPARABÉNS! Acertaste, era o numero {randomNum} e acertaste depois de {i} tentativas.\n")
                    input("Prima ENTER para voltar ao menu inicial...")
                    break
            else:
                input("Prima ENTER para voltar ao menu inicial...")

        case "0":
            exit() # SAÍ DO PROGRAMA