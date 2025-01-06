import json
import random
import string
from tabulate import tabulate

class AgilStore:
    def __init__(self, arquivo="inventario.json"):
        self.arquivo = arquivo
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r") as file:
                self.inventario = json.load(file)
        except FileNotFoundError:
            self.inventario = []

    def salvar_dados(self):
        with open(self.arquivo, "w") as file:
            json.dump(self.inventario, file, indent=4)

    def gerar_id(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=4))   
        return letras + numeros # concatenado

    def adicionar_produto(self):
        nome = input("Nome do Produto: ")
        categoria = input("Categoria: ")
        quantidade = int(input("Quantidade em Estoque: "))
        preco = float(input("Preço: "))
        produto = {
            "id": self.gerar_id(),
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco": preco
        }
        
        self.inventario.append(produto)
        self.salvar_dados()
        print(f"Produto adicionado com sucesso! ID: {produto['id']}")

    def listar_produtos(self):
        if not self.inventario:
            print("Nenhum produto cadastrado.")
            return
            
        tabela = [
            [p['id'], p['nome'], p['categoria'], p['quantidade'], f"R$ {p['preco']:.2f}"]
            for p in self.inventario
        ]
        print(tabulate(tabela, headers=["ID", "Nome", "Categoria", "Quantidade", "Preço"], tablefmt="grid"))

    def atualizar_produto(self):
        id_produto = input("ID do produto a ser atualizado: ").upper()
        produto = next((p for p in self.inventario if p['id'] == id_produto), None)
        if not produto:
            print("Produto não encontrado.")
            return

        print("Campos disponíveis para atualização:")
        print("[1] Nome\n[2] Categoria\n[3] Quantidade\n[4] Preço")
        opcao = input("Digite o número do campo que deseja atualizar: ").strip()

        campos = {
            "1": "nome",
            "2": "categoria",
            "3": "quantidade",
            "4": "preco"
        }

        campo = campos.get(opcao)
        if not campo:
            print("Opção inválida.")
            return

        novo_valor = input(f"Novo valor para {campo}: ")

        if campo == "quantidade":
            novo_valor = int(novo_valor)
        elif campo == "preco":
            novo_valor = float(novo_valor)

        produto[campo] = novo_valor
        self.salvar_dados()
        print("Produto atualizado com sucesso!")

    def excluir_produto(self):
        id_produto = input("ID do produto a ser excluído: ").upper()
        produto = next((p for p in self.inventario if p['id'] == id_produto), None)
        if not produto:
            print("Produto não encontrado.")
            return

        confirmacao = input(f"Tem certeza que deseja excluir o produto '{produto['nome']}'? (s/n): ").lower()

        if confirmacao == "s":
            self.inventario.remove(produto)
            self.salvar_dados()
            print("Produto excluído com sucesso!")
        else:
            print("Ação cancelada.")

    def buscar_produto(self):
        termo = input("Buscar por ID ou Nome (parte do nome): ").lower()
        resultados = [
            p for p in self.inventario if termo in p['id'].lower() or
            termo in p['nome'].lower()
        ]

        if not resultados:
            print("Nenhum produto encontrado.")
            return

        tabela = [
            [p['id'], p['nome'], p['categoria'], p['quantidade'], f"R$ {p['preco']:.2f}"]
            for p in resultados
        ]
        print(tabulate(tabela, headers=["ID", "Nome", "Categoria", "Quantidade", "Preço"], tablefmt="grid"))