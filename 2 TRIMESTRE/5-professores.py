import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor

    #O PYTHON RECLAMA DE "INCORRECT NUMBER OF BINDINGS".
    #ESTAMOS PASSANDO A VARIÁVEL, POR QUE OCORRE O ERRO?
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof))
    resultado = cursor. fetchone()
    print(resultado)
    conexao.close()