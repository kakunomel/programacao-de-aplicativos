import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("\nID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))
    conexao.commit()
    print("Escola deletada com sucesso!\n")
    conexao.close()

deletar_escola_antiga()