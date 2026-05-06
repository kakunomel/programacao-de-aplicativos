livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hadware"]
print(f"Livros disponíveis: {livros_disponiveis}")
livros_emprestados = []
print(f"Livros emprestados: {livros_emprestados}")

pedido = input("Digite o nome do livro que deseja: ")

if pedido in livros_disponiveis:
    livros_disponiveis.remove(pedido)
    livros_emprestados.append(pedido)
    print("Empréstimo realizado com sucesso!")
else:
    print("Desculpe, este livro não está no acervo.")

print("____________________________________________________")
print("                                                    ")

livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hadware"]
print(f"Livros disponíveis: {livros_disponiveis}")
livros_emprestados = [pedido]
print(f"Livros emprestados: {livros_emprestados}")

devolucao = input("Digite o nome do livro que está devolvendo: ")

if devolucao in livros_emprestados:
    livros_emprestados.remove(devolucao)
    devolucao.append(livros_disponiveis)
    print(f"Lista de livros disponíveis atualizada: {livros_disponiveis} ")
else:
    print("Este livro não consta como emprestado.")

print("____________________________________________________")  
print("                                                    ")

del livros_disponiveis[0:1]
print("RELATÓRIO FINAL")
print(f"Livros disponíveis: {livros_disponiveis}")
print(f"Livros emprestados: {livros_emprestados}")