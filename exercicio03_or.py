usuario = input("Digite seu nome de usuário:")
senha = input("Digite a senha:")

if (usuario == "admin" or usuario == "root") and senha == "12345":
    print("Acesso liberado!")
else:
    print("Acesso negado!")