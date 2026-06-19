import sqlite3 
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()
opcao = 0




def cadastrar():
    cursor.execute (''' 
                    CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT NOT NULL,
                    telefone_aluno TEXT,
                    turma_aluno TEXT,
                    idade_aluno INTEGER,
                    cpf_aluno TEXT UNIQUE NOT NULL,
                    endereco_aluno TEXT,
                    cidade_aluno TEXT,
                    estado_aluno TEXT
                    )''')

    print("\n----CADASTRO----")
    nome_aluno = input("Digite seu nome: ")
    telefone_aluno = input("Digite seu telefone: ")
    turma_aluno = input("Digite sua turma: ")
    idade_aluno = int(input("Digite sua idade: "))
    cpf_aluno = input("Digite seu CPF: ")
    endereco_aluno = input("Digite seu endereço: ")
    cidade_aluno = input("Digite sua cidade: ")
    estado_aluno = input("Digite seu estado: ")
    print("-" * 40)

    comando_inserir = (f''' 
                        INSERT INTO alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno, endereco_aluno, cidade_aluno, estado_aluno)
                        VALUES ('{nome_aluno}' , '{telefone_aluno}' , '{turma_aluno}' , '{idade_aluno}' , '{cpf_aluno}' , '{endereco_aluno}' , '{cidade_aluno}' , '{estado_aluno}')''')

    cursor.execute(comando_inserir)
    conexao.commit()




def listar():
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
            print(f"Endereço: {aluno[6]}")
            print(f"Cidade: {aluno[7]}")
            print(f"Estado: {aluno[8]}")
            print("-" * 50)




def alterar():
    listar()
    print("\n----EDITAR ALUNOS----")
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_turma = input("Digite a nova turma: ")
    nova_idade = int(input("Digite a nova idade: "))
    novo_cpf = input("Digite o novo CPF: ")
    novo_endereco = input("Digite o novo endereço: ")
    nova_cidade = input("Digite a nova cidade: ")
    novo_estado = input("Digite o novo estado: ")

    atualizar = f'''
    UPDATE Alunos
    SET nome_aluno = '{novo_nome}',
        telefone_aluno = '{novo_telefone}',
        turma_aluno = '{nova_turma}',
        idade_aluno = '{nova_idade}',
        cpf_aluno = '{novo_cpf}',
        endereco_aluno = '{novo_endereco}',
        cidade_aluno = '{nova_cidade}',
        estado_aluno = '{novo_estado}',
    WHERE id = {id_aluno}'''

    cursor.execute(atualizar)
    conexao.commit()

    if cursor.rowcount > 0:
        print("ALUNO ATUALIZADO COM SUCESSO!")
        print("-" * 50)
    else:
        print("NENHUM ALUNO ENCONTRADO COM ESSE ID.")
        print("-" * 50)




def excluir():        
    listar()
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




while opcao != 5:
    print("\n1 - CADASTRAR ALUNO")
    print("2 - LISTAR ALUNO")
    print("3 - EDITAR ALUNO")
    print("4 - EXCLUIR ALUNO")
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

conexao.close()
print("\nENCERRANDO PROGRAMA...")