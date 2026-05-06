print("----VALIDADOR DE SENHA----")

senha = input("\nDigite a senha: ")

def senha_valida (senha_usuario):
    while len(senha_usuario) < 6:
        senha_usuario = input("\nDigite a senha: ")
    print("Senha cadastrada com sucesso!")

senha_valida(senha)