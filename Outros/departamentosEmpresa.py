"""
    Lista de Departamentos de uma Empresa com listas
    @pedro.reis     27.out.2025
"""

lista = []

def asteriscos():
    print("*" * 52) # Imprime linha de 30 hífens

print("== LISTA DE DEPARTAMENTOS DE UMA EMPRESA ==")
print("Programador: Pedro Reis\n")

numDep = int(input("Indique o número de departamentos >> "))

for i in range (1, numDep + 1):
    nome = input(f"Nome do {i}.º departamento >> ")
    lista.append(nome)

asteriscos()
print("Inseriu os seguintes elementos por ordem alfabética:")
lista.sort()
for i in lista:
    print(f"\t- {i}")
asteriscos()

input("Prima ENTER para terminar...")
