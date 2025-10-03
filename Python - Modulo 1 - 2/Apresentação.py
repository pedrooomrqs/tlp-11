"""
    Input e Output de dados
    @pedro.reis     22.set.2025
"""

# Titulo do Programa
print("BEM VINDO AO CURSO PYTHON!")
print("Insira os seguintes dados ->")

# Entrada de Dados
nome = input("Digite o seu nome: ")
idade = int(input("Agora diz-me a tua idade: "))
custo_curso = float(input("Qual o custo do curso: "))

# Processamento
if (idade > 70 or idade < 10):
    print("ERRO! Não podes entrar no curso", nome)

else:
    print("Foste aceito na formação", nome)
    print("O custo indicado é de", custo_curso)

# Finalização
input("Prima <ENTER> para terminar.")