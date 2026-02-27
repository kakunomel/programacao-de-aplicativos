usuario = input("Digite o seu nome de usuário:")
codigo = int(input("Digite o código secreto:"))

if usuario == "admin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online.")
else:
    print("Falha na autenticação. Alerta de segurança ligado.")