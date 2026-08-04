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


def tabela_medico():
    conexao = sqlite3.connect('sistema_hospital.db')
    cursor = conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm INTEGER,
                FOREIGN KEY (id_hospital) REFERENCES hospitais(id))
                ''')

    print("-----CADASTRAR MÉDICO-----")
    nome_medico = input("Digite o nome do médico: ")
    crm = int(input("Digite o CRM do médico: "))