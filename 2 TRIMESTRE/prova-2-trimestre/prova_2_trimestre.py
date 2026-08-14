import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS cooperativas_teatro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cooperativa TEXT NOT NULL,
                registro_cultural TEXT NOT NULL)
                ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS teatros_fisicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_teatro TEXT NOT NULL,
                id_cooperativa INTEGER,
                FOREIGN KEY (id_cooperativa) REFERENCES cooperativas_teatro(id))
                ''')
    
    conexao.commit()
    conexao.close()
    print("\nTabelas criada com sucesso!")





def cadastrar_cooperativa():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    
    print("\n----- CADASTRAR COOPERATIVAS DE TEATRO -----")
    nome_cooperativa = input("\nDigite o nome da Cooperativa: ")
    registro_cultural = input("Digite o Registro Cultural: ")

    cursor.execute("INSERT INTO cooperativas_teatro (nome_cooperativa, registro_cultural) VALUES (?,?)",
    (nome_cooperativa, registro_cultural))
    conexao.commit()
    conexao.close()

    print("\nCooperativa cadastrada com sucesso!")





def listar_cooperativas():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM cooperativas_teatro")
        listar = cursor.fetchall()

        print("\n----- COOPERATIVAS CADASTRADAS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome: {l[1]}")
            print(f"Registro Cultural: {l[2]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def atualizar_cooperativa():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    listar_cooperativas()

    print("\n----- ATUALIZAR COOPERATIVA -----")

    try:
        id_cooperativa = int(input("\nInforme o ID da cooperativa que deseja alterar: "))
        nova_cooperativa = input("Digite o novo nome: ")
        novo_registro_cultural = input("Digite o novo registro: ")

        cursor.execute( "UPDATE cooperativas_teatro SET nome_cooperativa = ?, registro_cultural = ? WHERE id = ?",
        (nova_cooperativa, novo_registro_cultural, id_cooperativa))
        conexao.commit()
        print("\nCooperativa atualizada com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def excluir_cooperativa():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    listar_cooperativas()

    print("\n----- EXCLUIR COOPERATIVA -----")

    try:
        id_cooperativa = int(input("Digite o ID da Cooperativa que deseja excluir: "))


        deletar = f"DELETE FROM cooperativas_teatro WHERE id = {id_cooperativa}"
        cursor.execute(deletar)
        conexao.commit()
        print("Cooperativa excluida com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def cadastrar_teatro():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    print("\n----- CADASTRAR TEATROS FÍSICOS -----")
    try:
        nome_teatro = input("\nDigite o nome do teatro: ")
        id_cooperativa = int(input("Digite o ID da Cooperativa: "))

        cursor.execute("INSERT INTO teatros_fisicos (nome_teatro, id_cooperativa) VALUES (?,?)",
        (nome_teatro, id_cooperativa))
        conexao.commit()
        print("\nTeatro cadastrado com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")

    except sqlite3.IntegrityError:
        print("\nEssa cooperativa não existe!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def listar_teatros():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM teatros_fisicos")
        listar = cursor.fetchall()

        print("\n----- TEATROS CADASTRADOS -----")
        for l in listar:
            print(f"\nID Teatro: {l[0]}")
            print(f"Nome: {l[1]}")
            print(f"ID Cooperativa: {l[2]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def atualizar_teatro():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    listar_teatros()

    print("\n----- ATUALIZAR TEATRO -----")

    try:
        id_teatro = int(input("\nInforme o ID do teatro que deseja alterar: "))
        novo_teatro = input("Digite o novo nome: ")
        novo_id_cooperativa = input("Digite o ID da cooperativa: ")

        cursor.execute( "UPDATE teatros_fisicos SET nome_teatro = ?, id_cooperativa = ? WHERE id = ?",
        (novo_teatro, novo_id_cooperativa, id_teatro))
        conexao.commit()
        print("\nTeatro atualizada com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def excluir_teatro():
    conexao = sqlite3.connect('companhia_teatro.db')
    cursor = conexao.cursor()
    listar_teatros()

    print("\n----- EXCLUIR TEATRO -----")

    try:
        id_teatro = int(input("Digite o ID do Teatro que deseja excluir: "))


        deletar = f"DELETE FROM teatros_fisicos WHERE id = {id_teatro}"
        cursor.execute(deletar)
        conexao.commit()
        print("Teatro excluido com sucesso!")

    except ValueError:
        print("\nDigite apenas números!")
    
    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()





def menu():
    print("\n----- SISTEMA DE COMPANHIA DE TEATRO -----")
    while True:
        print("\n1 - CADASTRAR COOPERATIVA")
        print("2 - LISTAR COOPERATIVAS")
        print("3 - ATUALIZAR COOPERATIVA")
        print("4 - EXCLUIR COOPERATIVA")
        print("\n5 - CADASTRAR TEATRO")
        print("6 - LISTAR TEATROS")
        print("7 - ATUALIZAR TEATRO")
        print("8 - EXCLUIR TEATRO")
        print("9 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            cadastrar_cooperativa()

        elif opcao == "2":
            listar_cooperativas()

        elif opcao == "3":
            atualizar_cooperativa()

        elif opcao == "4":
            excluir_cooperativa()

        elif opcao == "5":
            cadastrar_teatro()

        elif opcao == "6":
            listar_teatros()

        elif opcao == "7":
            atualizar_teatro()

        elif opcao == "8": 
            excluir_teatro()

        elif opcao == "9":
            print("\nSaindo do programa...\n")
            break

criar_tabelas()
menu()