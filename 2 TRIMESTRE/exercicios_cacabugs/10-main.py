import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT alunos.nome_aluno, series.nome_serie
        FROM alunos 
        INNER JOIN series
        ON alunos.id_serie = series.id ''')

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conexao.close()

listar_alunos_e_turmas()