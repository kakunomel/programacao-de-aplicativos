usuario1 = input("Digite o nome de um pesquisador: ")

print("_________________________________________________________________")
print("                                                                 ")

nome =["Alice", "Bob", "Carlos"]

if usuario1 in nome:
    indice = nome.index(usuario1)
    print(f"Acesso Permitido! O pesquisador {usuario1} está na posição {indice}.")

    usuario2 = input("Deseja remover esse pesquisador da lista (Sim/Não): ")
    if usuario2 == "Sim":
        nome.remove(usuario1)
        print(f"Usuário {usuario1} removido.")
        print("Lista atualizada: " , nome)
    else:
        print("Programa Finalizado!")

else:
    print(f"Acesso Negado! O pesquisador {usuario1} não foi encontrado.")

    usuario3 = input("Deseja cadastrar esse novo pesquisador (Sim/Não): ")
    if usuario3 == "Sim":
        nome.append(usuario1)
        print(f"Nome do novo pesquisador cadastrado: {usuario1}")
        print(f"Lista atualizada: " , nome)
    else:
        print("Programa Finalizado!")

    print("_________________________________________________________________")
    print("                                                                 ")