import sqlite3 
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()


def cadastrar():
    cursor.execute (''' 
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_professor TEXT NOT NULL,
                    telefone_professor TEXT,
                    materia_professor TEXT,
                    idade_professor INTEGER,
                    cpf_professor TEXT UNIQUE NOT NULL
                    salario_professor TEXT,
                    escola_professor TEXT
                    )''')


    nome_professor = input("Digite o seu nome: ")
    telefone_professor = input("Digite seu telefone:")
    materia_professor = input("Digite a matéria que você da aula: ")
    idade_professor = int(input("Digite sua idade: "))
    cpf_professor = input("Digite seu CPF: ")
    salario_professor = input("Digite seu salário: ")
    nome_escola = input("Digite o nome da escola que você da aula: ")


    comando_inserir = (f'''
                        INSERT INTO professores (nome_professor, telefone_professor, materia_professor,
                        idade_professor, cpf_professor, salario_professor, escola_professor)
                        VALUES ('{nome_professor}' , '{telefone_professor}' , '{materia_professor}' , '{idade_professor}' ,
                        '{cpf_professor}' , '{salario_professor})' , '{nome_escola}''')


    cursor.execute(comando_inserir)
    conexao.commit
    conexao.close




def listar():
    cursor.execute("SELECT * FROM alunos")

    listar_professores = cursor.fetchall()

    print("\n-----PROFESSORES CADASTRADOS-----")

    if not listar_professores:
        print("\nNenhum professor cadastrado!")

    else:
        for prof in listar_professores:
            print(f"\nID: {prof[0]}")
            print(f"Nome: {prof[1]}")
            print(f"Telefone: {prof[2]}")
            print(f"Matéria: {prof[3]}")
            print(f"Idade: {prof[4]}")
            print(f"CPF: {prof[5]}")
            print(f"Salário: {prof[6]}")
            print(f"Escola: {prof[7]}")
            print("-" * 30)

    conexao.close()




def alterar():
    listar()
    id_professor = int(input("Digite o ID do professor que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_materia = input("Digite a nova matéria: ")
    nova_idade = int(input("Digite a nova idade: "))
    novo_cpf = input("Digite o novo CPF: ")
    novo_salario = input("Digite o novo salário: ")
    nova_escola = input("Digite nova escola: ")

    atualizar = f'''
    UPDATE professores
    SET nome_professor = '{novo_nome}',
        telefone_professor = '{novo_telefone}',
        materia_professor = '{nova_materia}',
        idade_professor = '{nova_idade}',
        cpf_professor = '{novo_cpf}',
        salario_professor = '{novo_salario}',
        escola_professor = '{nova_escola}
    WHERE id = {id_professor}'''

    cursor.execute(atualizar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Professor atualizado com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")

    conexao.close()




def excluir():

    id_professor = int(input("Digite o ID do professor que deseja excluir: "))

    deletar = f"DELETE FROM Alunos WHERE id = {id_professor}"

    cursor.execute(deletar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Professor excluído com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")

    conexao.close()

while opcao != 5:
    print("\n1 - CADASTRAR PROFESSOR")
    print("2 - LISTAR PROFESSORES")
    print("3 - EDITAR PROFESSORES")
    print("4 - EXCLUIR PROFESSORES")
    print("5 - SAIR")

    opcao = int(input("\nDigite a opção que deseja: "))

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        listar()

    elif opcao == 3:
        alterar()

    elif opcao == 4:
        excluir()

print("Encerrando programa...")