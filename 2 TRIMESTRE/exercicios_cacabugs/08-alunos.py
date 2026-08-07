import sqlite3

def atualizar_nome_aluno():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute( "UPDATE alunos SET nome_aluno = ? WHERE id = ?", (novo_nome, id_aluno))
    conexao.commit()
    print("Aluno atualizado com sucesso!")
    conexao.close()

id_aluno = int(input("Informe o ID do aluno que deseja alterar: "))
novo_nome = input("Digite o novo nome: ")

atualizar_nome_aluno()