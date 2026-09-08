import sqlite3

def cadastrar_aluno():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    
    print("\n----- CADASTRAR ALUNO -----")

    try:
        nome_aluno = input("\nQual seu nome: ")
        idade_aluno = int(input("Digite sua idade: "))
        id_turma = input("Digite o ID da sua turma: ")

        cursor.execute("INSERT INTO alunos (nome_aluno, idade_aluno, id_turma) VALUES (?,?)",
        (nome_aluno, idade_aluno, id_turma))
        
        conexao.commit ()
        print("\nAluno cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("\nErro..." , e)

    finally:
        conexao.close()



def listar_aluno():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM alunos")
        listar = cursor.fetchall()

        print("\n----- ALUNOS CADASTRADOS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Aluno: {l[1]}")
            print(f"Idade: ")
            print(f"ID Turma: {l[2]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def atualizar_aluno():
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

    print("\n----- ATUALIZAR ALUNO -----")

    try:
        listar_aluno()
        id_aluno = int(input("\nInforme o ID do aluno que deseja alterar: "))
        novo_nome = input("Digite o novo nome: ")
        nova_idade = int(input("Digite a nova idade: "))

        cursor.execute( "UPDATE alunos SET novo_nome = ?, nova_cidade = ? WHERE id = ?",
        (novo_nome, nova_idade, id_aluno))
        conexao.commit()
        print("\nAluno atualizada com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def excluir_escola():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    print("\n----- EXCLUIR ALUNO -----")

    try:
        listar_aluno()
        id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
        deletar = f"DELETE FROM alunos WHERE id = {id_aluno}"
        cursor.execute(deletar)
        conexao.commit()
        print("Aluno excluida com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()