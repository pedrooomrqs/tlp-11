"""
Calculadora de IMC 
Feito por: Pedro e Ulisses
"""
import math

print("---Calculadora de IMC---\n")

altura = float(input("Qual a sua altura (em metros) >> "))
peso = float(input("Qual o seu peso >> "))

imc = peso / (altura*altura)

print("\nO seu IMC é de: %.2f" % imc)

if (imc < 18.5):
    print("\nVocê está abaixo do peso.")

elif (imc >= 18.5 and imc < 24.9):
    print("\nVocê está com o peso normal.")

elif (imc >= 25 and imc < 29.9):
    print("\nVocê está em sobrepeso.")

elif (imc >= 30):
    print("\nVocê está com obesidade grau 1.")

elif (imc >= 35 and imc < 39.9):
    print("\nVocê está com obesidade grau 2.")

elif (imc >= 40):
    print("\nVocê está com obesidade grau 3.")

else:
    print("\nErro!")

input("\nPrima <ENTER> para terminar.")