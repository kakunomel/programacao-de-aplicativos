import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXIXTS professores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_professor TEXT NOT NULL)''')

    nome_professor = input("\nDigite o nome do profesor: ")
    conexao.commit()

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()

    if resultado:
        print("Professor encontrado:" resultado)
    else:
        print("Professor não encontrado!")

    conexao.close()

buscar_professor(1)