def menu():
    while True:
        print("\n1 - Cadastrar Aluno")
        print("2 - Sair")
        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\nCadastrando...\n")
        elif opcao == "2":
            print("\nSaindo do programa...\n")
            break
menu()