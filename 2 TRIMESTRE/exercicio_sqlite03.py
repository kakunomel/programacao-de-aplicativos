import sqlite3 
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()
opcao = 0



def cadastrar_professor():
    cursor.execute (''' 
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_professor TEXT NOT NULL,
                    telefone_professor TEXT,
                    materia_professor TEXT,
                    idade_professor INTEGER,
                    cpf_professor TEXT UNIQUE NOT NULL,
                    salario_professor TEXT,
                    escola_professor TEXT
                    )''')

    print("\n---- CADASTRO ----")
    nome_professor = input("Digite o seu nome: ")
    telefone_professor = input("Digite seu telefone: ")
    materia_professor = input("Digite a matéria que você da aula: ")
    idade_professor = int(input("Digite sua idade: "))
    cpf_professor = input("Digite seu CPF: ")
    salario_professor = input("Digite seu salário: ")
    nome_escola = input("Digite o nome da escola que você da aula: ")
    print("-" * 50)


    inserir = (f'''
                INSERT INTO professores (nome_professor, telefone_professor, materia_professor,
                idade_professor, cpf_professor, salario_professor, escola_professor)
                VALUES ('{nome_professor}' , '{telefone_professor}' , '{materia_professor}' , '{idade_professor}' ,
                '{cpf_professor}' , '{salario_professor}' , '{nome_escola}')''')


    cursor.execute(inserir)
    conexao.commit()



def listar_professor():
    cursor.execute("SELECT * FROM professores")

    listar_professores = cursor.fetchall()

    print("\n-----PROFESSORES CADASTRADOS-----")

    if not listar_professores:
        print("\nNENHUM PROFESSOR CADASTRADO!")

    else:
        for prof in listar_professores:
            print(f"ID: {prof[0]}")
            print(f"Nome: {prof[1]}")
            print(f"Telefone: {prof[2]}")
            print(f"Matéria: {prof[3]}")
            print(f"Idade: {prof[4]}")
            print(f"CPF: {prof[5]}")
            print(f"Salário: {prof[6]}")
            print(f"Escola: {prof[7]}")
            print("-" * 50)



def alterar_professor():
    listar_professor()
    print("\n----EDITAR PROFESSOR----")
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
        escola_professor = '{nova_escola}'
    WHERE id = {id_professor}'''

    cursor.execute(atualizar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("PROFESSOR ATUALIZADO COM SUCESSO!")
        print("-" * 50)
    else:
        print("NENHUM PROFESSOR ENCONTRADO COM ESSE ID.")
        print("-" * 50)



def excluir_professor():
    listar_professor()
    print("\n----EXCLUIR PROFESSOR----")
    id_professor = int(input("Digite o ID do professor que deseja excluir: "))

    deletar = f"DELETE FROM professores WHERE id = {id_professor}"
    cursor.execute(deletar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("PROFESSOR EXCLUIDO COM SUCESSO!")
        print("-" * 50)
    else:
        print("NENHUM PROFESSOR ENCONTRADO COM ESSE ID.")
        print("-" * 50)





def cadastrar_aluno():
    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT NOT NULL,
                    telefone_aluno TEXT,
                    turma_aluno TEXT,
                    idade_aluno INTEGER,
                    cpf_aluno TEXT UNIQUE NOT NULL,
                    professor_id INTEGER,
                    FOREIGN KEY (professor_id) REFERENCES professores(id)
                    )''')

    print("\n----CADASTRO----")
    nome_aluno = input("Digite seu nome: ")
    telefone_aluno = input("Digite seu telefone: ")
    turma_aluno = input("Digite sua turma: ")
    idade_aluno = int(input("Digite sua idade: "))
    cpf_aluno = input("Digite seu CPF: ")
    listar_professor()
    professor_id = int(input("Digite o ID do professor que deseja: "))
    print("-" * 50)

    comando_inserir = (f''' 
                        INSERT INTO alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, professor_id)
                        VALUES ('{nome_aluno}' , '{telefone_aluno}' , '{turma_aluno}' , '{idade_aluno}' , '{cpf_aluno}' , '{professor_id}')''')

    cursor.execute(comando_inserir)
    conexao.commit()



def listar_aluno():
    cursor.execute("SELECT * FROM alunos")

    todos_alunos = cursor.fetchall()

    print("\n-----ALUNOS CADASTRADOS-----")

    if not todos_alunos:
        print("NENHUM ALUNO CADASTRADO!")

    else:
        for aluno in todos_alunos:
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Telefone: {aluno[2]}")
            print(f"Turma: {aluno[3]}")
            print(f"Idade: {aluno[4]}")
            print(f"CPF: {aluno[5]}")
            print("-" * 50)



def alterar_aluno():
    listar_aluno()
    print("\n----EDITAR ALUNOS----")
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_turma = input("Digite a nova turma: ")
    nova_idade = int(input("Digite a nova idade: "))
    novo_cpf = input("Digite o novo CPF: ")

    atualizar = f'''
    UPDATE Alunos
    SET nome_aluno = '{novo_nome}',
        telefone_aluno = '{novo_telefone}',
        turma_aluno = '{nova_turma}',
        idade_aluno = '{nova_idade}',
        cpf_aluno = '{novo_cpf}'
    WHERE id = {id_aluno}'''

    cursor.execute(atualizar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("ALUNO ATUALIZADO COM SUCESSO!")
        print("-" * 50)
    else:
        print("NENHUM ALUNO ENCONTRADO COM ESSE ID.")
        print("-" * 50)



def excluir_aluno():        
    listar_aluno()
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

    deletar = f"DELETE FROM Alunos WHERE id = {id_aluno}"

    cursor.execute(deletar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("ALUNO EXCLUÍDO COM SUCESSO!")
        print("-" * 50)
    else:
        print("NENHUM ALUNO ENCONTRADO COM ESSE ID.")
        print("-" * 50)



while opcao != 9:
    print("\n1 - CADASTRAR ALUNO")
    print("2 - LISTAR ALUNO")
    print("3 - EDITAR ALUNO")
    print("4 - EXCLUIR ALUNO\n")
    print("5 - CADASTRAR PROFESSOR")
    print("6 - LISTAR PROFESSORES")
    print("7 - EDITAR PROFESSOR")
    print("8 - EXCLUIR PROFESSOR")
    print("9 - SAIR")
    opcao = int(input("\nDigite a opção que deseja: "))

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        listar_aluno()

    elif opcao == 3:
        alterar_aluno()

    elif opcao == 4:
        excluir_aluno()

    elif opcao == 5:
        cadastrar_professor()

    elif opcao == 6:
        listar_professor()

    elif opcao == 7:
        alterar_professor()

    elif opcao == 8:
        excluir_professor()

conexao.close()
print("\nENCERRANDO PROGRAMA...\n")