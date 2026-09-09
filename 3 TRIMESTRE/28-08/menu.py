from banco import tabela_escolas, tabela_turmas, tabela_alunos
from escola import cadastrar_escolas, listar_escolas, atualizar_escola, excluir_escola
from turma import cadastrar_turma, listar_turma, atualizar_turma, excluir_turma
from aluno import cadastrar_aluno, listar_aluno, atualizar_aluno, excluir_aluno

def menu():
    while True:
        print("\n----- SISTEMA DE GESTÃO ESCOLAR -----")
        print("\n1 - ESCOLA")
        print("2 - TURMA")
        print("3 - ALUNOS")
        print("4 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            crud_escola()

        elif opcao == "2":
            crud_turma()

        elif opcao == "3":
            crud_aluno()

        elif opcao == "4":
            print("\nSaindo do programa...\n")
            break



def crud_escola():
    print("\n----- CRUD ESCOLA -----")
    while True:
        print("\n1 - CADASTRAR ESCOLA")
        print("2 - LISTAR ESCOLAS")
        print("3 - ATUALIZAR ESCOLA")
        print("4 - EXCLUIR ESCOLA")
        print("5 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            cadastrar_escolas()

        elif opcao == "2":
            listar_escolas()

        elif opcao == "3":
            atualizar_escola()

        elif opcao == "4":
            excluir_escola()

        elif opcao == "5":
            print("\nSaindo do programa...\n")
            break


def crud_turma():
    print("\n----- CRUD TURMA -----")
    while True:
        print("\n1 - CADASTRAR TURMA")
        print("2 - LISTAR TURMAS")
        print("3 - ATUALIZAR TURMA")
        print("4 - EXCLUIR TURMA")
        print("5 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            cadastrar_turma()

        elif opcao == "2":
            listar_turma()

        elif opcao == "3":
            atualizar_turma()

        elif opcao == "4":
            excluir_turma()

        elif opcao == "5":
            print("\nSaindo do programa...\n")
            break


def crud_aluno():
    print("\n----- CRUD ALUNO -----")
    while True:
        print("\n1 - CADASTRAR ALUNO")
        print("2 - LISTAR ALUNOS")
        print("3 - ATUALIZAR ALUNO")
        print("4 - EXCLUIR ALUNO")
        print("5 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_aluno()

        elif opcao == "3":
            atualizar_aluno()

        elif opcao == "4":
            excluir_aluno()

        elif opcao == "5":
            print("\nSaindo do programa...\n")
            break

menu()