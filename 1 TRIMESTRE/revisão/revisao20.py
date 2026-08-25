print("\n-----CARRINHO DE COMPRAS INTERATIVO-----")

produtos = []
adicionar = ""

while adicionar != "sair":
    adicionar = input("\nDigite o nome do produto (ou 'sair' para finalizar): ")

    if adicionar != "sair":
        produtos.append(adicionar)
      
print("\nProdutos adicionados ao carrinho:")
print(produtos) 