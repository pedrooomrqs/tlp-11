import os

def inserir_produtos(produto1, preco1, lista):
    pass

def reset_lista(lista):
    pass

def hifenes():
    print("-" * 50)

def menu(lista_produtos):
    opcao="10"
    while True:
        os.system("cls")
        hifenes()
        print("\nBem-vindo à Loja V")
        print("Curso Profissional de Programador")
        print("Desenvolvedor: Pedro Reis")
        hifenes()
        print("\nLoja de roupa\nMENU\n")
        print("[1] Reset da lista de artigos")
        print("[2] Inserir artigos na loja")
        print("[3] Listar artigos da loja")
        print("[4] Valor do stock em €")
        print("[0] Sair da loja")
        hifenes()

        opcao=input("\nOpção >> ")
        match opcao:
            case "1":
                lista_produtos = reset_lista(lista_produtos)
            case "2":
                produto = input("\nIndique o produto a inserir >> ")
                preco = float(input("Indique o preço >> "))
                lista_produtos = inserir_produtos(produto, preco, lista_produtos)
                print("\nProduto inserido com sucesso!")
            case "3":
                print("\nOs produtos da loja são: ")
                ver_produtos(lista_produtos)
            case "4":
                print("\nO valor do stock em € é: ")
                print(f"\t {valor_stock(lista_produtos)}€")
            case "0":
                print("\nSaída da loja")
                opcao = "0"
            case _:
                print("\nERRO! Opção inválida.")
        input("\nPrima ENTER para continuar...")

# PROGRAMA PRINCIPAL
lista_produtos=[]
menu(lista_produtos)

input("\nPrima ENTER para terminar.")