import sqlite3


def criar_tabelas():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS laboratorio_informatica1(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_solicitante TEXT NOT NULL,
                laboratorio_inf1 TEXT NOT NULL,
                data_inf1 TEXT NOT NULL,
                horario_inf1 TEXT NOT NULL)''')

   
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS laboratorio_informatica2(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_solicitante TEXT NOT NULL,
                laboratorio_inf2 TEXT NOT NULL,
                data_inf2 TEXT NOT NULL,
                horario_inf2 TEXT NOT NULL)''')


    cursor.execute('''
            CREATE TABLE IF NOT EXISTS laboratorio_robotica(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_solicitante TEXT NOT NULL,
            laboratorio_rbtc TEXT NOT NULL,
            data_rbtc TEXT NOT NULL,
            horario_rbtc TEXT NOT NULL)''')


    cursor.execute('''
            CREATE TABLE IF NOT EXISTS laboratorio_eletroeletronica(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_solicitante TEXT NOT NULL,
            laboratorio_eletro TEXT NOT NULL,
            data_eletro TEXT NOT NULL,
            horario_eletro TEXT NOT NULL)''')
    

    conexao.commit()
    conexao.close()
    print("\nTabelas criada com sucesso!")


def reservar_lab01():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()
    
    try:
        print("\n----- RESERVAR LABORATÓRIO INFORMÁTICA -----")
        nome_solicitante = input("\nDigite seu nome: ")
        laboratorio_inf1 = input("Digite o laboratório: ")
        data_inf1 = input("Digite a data: ")
        horario_inf1 = input("Digite o horário: ")

        cursor.execute("INSERT INTO laboratorio_informatica1 (nome_solicitante, laboratorio_inf1, data_inf1, horario_inf1) VALUES (?,?,?,?)",
        (nome_solicitante, laboratorio_inf1, data_inf1, horario_inf1))

    except sqlite3.Error as e:
        print("\nErro...", e)

    conexao.commit()
    conexao.close()
    print("\nLaboratorio reservado com sucesso!")

def listar_laboratorio1():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM laboratorio_informatica1")
        listar = cursor.fetchall()

        print("\n----- LABORATORIOS CADASTRADAS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome Solicitante: {l[1]}")
            print(f"Laboratorio: {l[2]}")
            print(f"Data: {l[3]}")
            print(f"Horário: {l[4]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()




def reservar_lab02():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()
    
    try:
        print("\n----- RESERVAR LABORATÓRIO INFORMÁTICA -----")
        nome_solicitante = input("\nDigite seu nome: ")
        laboratorio_inf2 = input("Digite o laboratório: ")
        data_inf2 = input("Digite a data: ")
        horario_inf2 = input("Digite o horário: ")

        cursor.execute("INSERT INTO laboratorio_informatica2 (nome_solicitante, laboratorio_inf2, data_inf2, horario_inf2) VALUES (?,?,?,?)",
        (nome_solicitante, laboratorio_inf2, data_inf2, horario_inf2))

    except sqlite3.Error as e:
        print("\nErro...", e)

    conexao.commit()
    conexao.close()
    print("\nLaboratorio reservado com sucesso!")

def listar_laboratorio2():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM laboratorio_informatica2")
        listar = cursor.fetchall()

        print("\n----- LABORATORIOS CADASTRADAS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome Solicitante: {l[1]}")
            print(f"Laboratorio: {l[2]}")
            print(f"Data: {l[3]}")
            print(f"Horário: {l[4]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()




def reservar_lab_rbtc():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()
    
    try:
        print("\n----- RESERVAR LABORATÓRIO ROBÓTICA -----")
        nome_solicitante = input("\nDigite seu nome: ")
        laboratorio_rbtc = input("Digite o laboratório: ")
        data_rbtc = input("Digite a data: ")
        horario_rbtc = input("Digite o horário: ")

        cursor.execute("INSERT INTO laboratorio_robotica (nome_solicitante, laboratorio_rbtc, data_rbtc, horario_rbtc) VALUES (?,?,?,?)",
        (nome_solicitante, laboratorio_rbtc, data_rbtc, horario_rbtc))

    except sqlite3.Error as e:
        print("\nErro...", e)

    conexao.commit()
    conexao.close()
    print("\nLaboratorio reservado com sucesso!")

def listar_lab_rbtc():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM laboratorio_robotica")
        listar = cursor.fetchall()

        print("\n----- LABORATORIOS CADASTRADOS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome Solicitante: {l[1]}")
            print(f"Laboratorio: {l[2]}")
            print(f"Data: {l[3]}")
            print(f"Horário: {l[4]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()



def reservar_lab_eletro():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()
    
    try:
        print("\n----- RESERVAR LABORATÓRIO ELETRO -----")
        nome_solicitante = input("\nDigite seu nome: ")
        laboratorio_rbtc = input("Digite o laboratório: ")
        data_rbtc = input("Digite a data: ")
        horario_rbtc = input("Digite o horário: ")

        cursor.execute("INSERT INTO laboratorio_eletroeletronica (nome_solicitante, laboratorio_eletro, data_eletro, horario_eletro) VALUES (?,?,?,?)",
        (nome_solicitante, laboratorio_eletro, data_eletro, horario_eletro))

    except sqlite3.Error as e:
        print("\nErro...", e)

    conexao.commit()
    conexao.close()
    print("\nLaboratorio reservado com sucesso!")

def listar_lab_eletro():
    conexao = sqlite3.connect('cadastro_laboratorios.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM laboratorio_eletroeletronica")
        listar = cursor.fetchall()

        print("\n----- LABORATORIOS CADASTRADOS -----")
        for l in listar:
            print(f"\nID: {l[0]}")
            print(f"Nome Solicitante: {l[1]}")
            print(f"Laboratorio: {l[2]}")
            print(f"Data: {l[3]}")
            print(f"Horário: {l[4]}")

    except sqlite3.Error as e:
        print("\nErro...", e)

    finally:
        conexao.close()


def menu():
    print("\n----- SISTEMA DE RESERVA DE LABORATÓRIOS -----")
    while True:
        print("\n1 - RELIZAR RESERVA LAB1")
        print("2 - RELIZAR RESERVA LAB2")
        print("3 - RELIZAR RESERVA LAB RBTC")
        print("4 - RELIZAR RESERVA LAB ELETRO")
        print("5 - CONSULTAR LAB1")
        print("6 - CONSULTAR LAB2")
        print("7 - CONSULTAR LAB RBTC")
        print("8 - CONSULTAR LAB ELETRO")
        print("9 - SAIR")
        opcao = input("\nDigite o que deseja: ")

        if opcao == "1":
            reservar_lab01()

        elif opcao == "2":
            reservar_lab02()

        elif opcao == "3":
            reservar_lab_rbtc()

        elif opcao == "4":
            reservar_lab_eletro()

        elif opcao == "5":
            listar_laboratorio1()

        elif opcao == "6":
            listar_laboratorio2()

        elif opcao == "7":
            listar_lab_rbtc()

        elif opcao == "8": 
            listar_lab_eletro()

        elif opcao == "9":
            print("\nSaindo do programa...\n")
            break
criar_tabelas()
menu()