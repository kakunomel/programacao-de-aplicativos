lista_vip = []
nome = ""

while nome != "fim":
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome != "fim":
        if nome[0] == "A":
            lista_vip.append(nome)
            print("Lista VIP: " , lista_vip)
        else:
            print("Apena nomes com A são permitidos no VIP")
print("Encerrando programa...")