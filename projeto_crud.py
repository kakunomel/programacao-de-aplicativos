print("\n---SISTEMA CRUD MODULARIZADO---")

estoque = []
nome_produtos = input("Digite os nomes dos produtos: ")
indice = ""
novo_nome = ""


def adicionar_produto(nome):
    estoque.append(nome_produtos)
    print(estoque)

def listar_produtos():
    for produto in nome_produtos:
        print(produto)

def atualizar_produto(indice, novo_nome):
    novo_nome = input("Digite o nome de um noo produto: ")
    
def remover_produto(indice):



def exibir_menu():

    print("1- Adicionar Produto")
    print("2- Listar Produtos")
    print("3- Atualizar Produto")
    print("4- Remover Produto")
    print("5- Sair")

    usuario = input("Digite a opção que deseja:")
    while usuario != 5
        if usuario == 1:
            print(adicionar_produto)

        elif usuario == 2:
            print(listar_produtos)

        elif usuario == 3:
            print(atualizar_produto)

        elif usuario == 4:
            print(remover_produto)

        else:
            print("Encerrando programa...")