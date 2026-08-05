import sqlite3


def tabela_hospital():
    conexao = sqlite3.connect('banco_hospital.db')
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS hospitais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL)
                ''')

    print("-----CADASTRAR HOSPITAL-----")
    nome_hospital = input("Digite o nome do hospital: ")
    cidade_hospital = input("Digite o nome da cidade do hospital: ")

    comando_inserir = (f'''
                        INSERT INTO hospitais (nome, cidade)
                        VALUES ('{nome_hospital}' , '{cidade_hospital}')''')
    cursor.execute(comando_inserir)
    conexao.commit()
    print("Hospital cadastrado com sucesso!")
    conexao.close()



def tabela_medico():
    conexao = sqlite3.connect('banco_hospital.db')
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm INTEGER,
                id_hospital INTEGER,
                FOREIGN KEY (id_hospital) REFERENCES hospitais(id))
                ''')

    print("\n-----CADASTRAR MÉDICO-----")
    try:
        nome_medico = input("Digite o nome do médico: ")
        crm = int(input("Digite o CRM do médico: "))
        id_hospital = int(input("Digite o ID do hospital que o médico trabalha: "))
        comando_inserir = (f''' INSERT INTO medicos (nome, crm, id_hospital)
                                VALUES ('{nome_medico}' , '{crm}' , '{id_hospital}')''')
        cursor.execute(comando_inserir)
        conexao.commit()
        print("Médico cadastrado com sucesso!\n")

    except ValueError:
        print("Digite apenas números!")
   
    finally:
        conexao.close()

tabela_hospital()
tabela_medico()