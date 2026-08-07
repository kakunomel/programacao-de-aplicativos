import sqlite3
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

cursor.execute('''DROP TABLE professores
''')
conexao.commit()