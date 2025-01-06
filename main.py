from AgilStore import AgilStore
from tabulate import tabulate

def main():
    loja = AgilStore()

    while True:
        menu_opcoes = [
            ["1", "Adicionar Produto"],
            ["2", "Listar Produtos"],
            ["3", "Atualizar Produto"],
            ["4", "Excluir Produto"],
            ["5", "Buscar Produto"],
            ["6", "Sair"]
        ]

        print("\n==== AgilStore - Gerenciamento de Inventário ====")
        print(tabulate(menu_opcoes, headers=["Opção", "Descrição"], tablefmt="grid"))
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.adicionar_produto()

        elif opcao == "2":
            loja.listar_produtos()

        elif opcao == "3":
            loja.atualizar_produto()

        elif opcao == "4":
            loja.excluir_produto()

        elif opcao == "5":
            loja.buscar_produto()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
