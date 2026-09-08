import sqlite3
conexao = sqlite3.connect('gestao_escolar.db')
cursor = conexao.cursor()

cursor.execute('''DROP TABLE alunos
''')
conexao.commit()