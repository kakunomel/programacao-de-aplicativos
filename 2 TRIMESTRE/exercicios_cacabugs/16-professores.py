import sqlite3

def inserir_professor():
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        nome_professor = input("\nDigite o nome do professor: ")
        materia_professor = input("Digite a matéria do professor: ")
        cpf_professor = int(input("Digite o CPF do professor: "))

        cursor.execute("INSERT INTO professores(nome_professor, materia_professor, cpf_professor) VALUES (?,?,?)", (nome_professor, materia_professor, cpf_professor))
        conexao.commit()
        print("Professor cadastrado com sucesso!\n")

    except sqlite3.Error as e:
        print("Erro: Este CPF já está cadastrado no sistema!" , e)
    
    finally:
        conexao.close()

inserir_professor()