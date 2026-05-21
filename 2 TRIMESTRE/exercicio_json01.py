print("\n------SISTEMA DE MATRÍCULA------")
usuario = 0


def menu():
    nome = input("\nDigite seu nome: ")
    cpf = int(input("Digite seu CPF: "))
    idade = int(input("Digite sua idade: "))
    telefone = int(input("Digite seu telefone: "))
    turma = input("Digite sua turma: ")


def opcoes():
    print("\n1- CADASTRAR ALUNO")
    print("2- LISTAR ALUNOS")
    print("3- EDITAR ALUNOS")
    print("4- EXCLUIR ALUNO")
    print("5- SAIR")
    usuario = int(input("\nDigite a opção que deseja: "))


def cadastrar_aluno():
    aluno = {
            "nome" : nome, 
            "idade" : idade,
            "CPF" : cpf,
            "telefone" : telefone,
            "turma" : turma
            }


def listar_alunos():

def atualizar_dados():

def remover_aluno():



while usuario != 5:
    opcoes()

    if usuario == 1:
        cadastrar_aluno()
    elif usuario == 2:
        listar_alunos()
    elif usuario == 3:
        atualizar_dados():
    elif usuario == 4:
        remover_aluno():
print("Encerrando programa...")
        