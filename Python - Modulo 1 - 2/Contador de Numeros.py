"""
    Contador de Numeros
    @pedro.reis     3.out.2025
"""
#Entrada de Dados
num1=int(input("1º Numero >> "))
num2=int(input("2º Numero >> "))
num3=int(input("3º Numero >> "))
num4=int(input("4º Numero >> "))
num5=int(input("5º Numero >> "))
num6=int(input("6º Numero >> "))

#Processamento de Dados
contador = 0
if (num1 >= 50 and num1 <= 100):
    contador = contador + 1
if (num2 >= 50 and num2 <= 100):
    contador = contador + 1
if (num3 >= 50 and num3 <= 100):
    contador = contador + 1
if (num4 >= 50 and num4 <= 100):
    contador = contador + 1
if (num5 >= 50 and num5 <= 100):
    contador = contador + 1
if (num6 >= 50 and num6 <= 100):
    contador = contador + 1

#Saída de dados
print("Total de numeros entre 50 e 100:", contador)