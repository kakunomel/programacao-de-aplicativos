import sqlite3

def cadastrar_turma():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    
    print("\n----- CADASTRAR TURMA -----")

    try:
        nome_turma = input("\nQual sua turma: ")
        id_escola = input("Digite o ID da sua escola: ")

        cursor.execute("INSERT INTO turmas (nome_turma, id_escola) VALUES (?,?)",
        (nome_turma, id_escola))
        
        conexao.commit ()
        print("\nTurma cadastrada com sucesso!")

    except sqlite3.Error as erro:
        print("\nErro..." , e)

    finally:
        conexao.close()



def listar_turma():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM turmas")
        listar = cursor.fetchall()

        print("\n----- TURMAS CADASTRADAS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Turma: {l[1]}")
            print(f"ID Escola: {l[2]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def atualizar_turma():
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

    print("\n----- ATUALIZAR TURMA -----")

    try:
        listar_turma()
        id_turma = int(input("\nInforme o ID da turma que deseja alterar: "))
        nova_turma = input("Digite a nova turma: ")

        cursor.execute( "UPDATE turmas SET novo_nome = ?, WHERE id = ?",
        (novo_nome, id_turma))
        conexao.commit()
        print("\nTurma atualizada com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def excluir_turma():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    print("\n----- EXCLUIR TURMA -----")

    try:
        listar_turma()
        id_turma = int(input("Digite o ID da turma que deseja excluir: "))
        deletar = f"DELETE FROM turmas WHERE id = {id_turma}"
        cursor.execute(deletar)
        conexao.commit()
        print("Turma excluida com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()