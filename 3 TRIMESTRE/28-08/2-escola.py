import sqlite3

def cadastrar_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    
    print("\n----- CADASTRAR ESCOLAS -----")

    try:
        nome_escola = input("\nDigite o nome da sua escola: ")
        nome_cidade = input("Digite o nome da sua cidade: ")
        assert nome_escola.strip() != "", "O nome da escola não pode ficar vazio"
        assert nome_cidade.strip() != "", "O nome da cidade não pode ficar vazio"

        cursor.execute("INSERT INTO escolas (nome_escola, nome_cidade) VALUES (?,?)",
        (nome_escola, nome_cidade))
        
        conexao.commit ()
        print("\nEscola cadastrada com sucesso!")
    
    except AssertionError as e:
        print("\nErro..." , e)

    except sqlite3.Error as erro:
        print("\nErro..." , e)

    finally:
        conexao.close()



def listar_escolas():
    conexao = sqlite3.connect('gestao_escolar.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM escolas")
        listar = cursor.fetchall()

        print("\n----- ESCOLAS CADASTRADAS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome Escola: {l[1]}")
            print(f"Cidade Escola: {l[2]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def atualizar_escola():
        conexao = sqlite3.connect('gestao_escolar.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

    print("\n----- ATUALIZAR ESCOLA -----")

    try:
        listar_escolas()
        id_escola = int(input("\nInforme o ID da escola que deseja alterar: "))
        novo_nome = input("Digite o novo nome: ")
        nova_cidade = input("Digite a nova cidade: ")

        cursor.execute( "UPDATE turmas SET novo_nome = ?, nova_cidade = ? WHERE id = ?",
        (novo_nome, nova_cidade, id_escola))
        conexao.commit()
        print("\nEscola atualizada com sucesso!")

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

    print("\n----- EXCLUIR ESCOLA -----")

    try:
        id_escola = int(input("Digite o ID da escola que deseja excluir: "))
        deletar = f"DELETE FROM escolas WHERE id = {id_escola}"
        cursor.execute(deletar)
        conexao.commit()
        print("Escola excluida com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()