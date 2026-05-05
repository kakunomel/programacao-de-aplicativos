print("\n------ANALISADOR DE TEXTO------")

usuario = input("Digite um nome de usuário: ")

def contar_caracteres (usuario):
    if len(usuario) < 5:
        print("Nome muito curto!")
    else:
        print("Nome aceito!")

contar_caracteres(usuario)