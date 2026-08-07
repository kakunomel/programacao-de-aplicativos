import sqlite3

def inserir_escola(nome_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas (nome_escola) VALUES (?)", (nome_escola,))
    conexao.commit()
    print("Escola cadastrada com sucesso!\n")
    conexao.close()

nome_escola = input("\nDigite o nome da escola: ")
inserir_escola(nome_escola)