import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    #O SISTEMA ACEITA CADASTRAR DOIS PROFESSORES COM O MESMO CPF.
    #COMO RESTRINGIR ISSO DIRETO NA ESTRUTURA DA ABELA ABAIXO?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTST professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cpf TEXT) ''')