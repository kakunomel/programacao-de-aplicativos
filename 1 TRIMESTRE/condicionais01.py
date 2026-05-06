nome = input("Digite o seu nome:")
altura = float(input("Digite a sua altura:"))

if altura < 1.50:
    print ("Desculpe, você não tem altura miníma" , nome)
elif altura >= 1.50:
    print ("Acesso liberado!Diverta-se na queda livre" , nome)