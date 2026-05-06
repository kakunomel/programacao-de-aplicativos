idade = int(input("Digite a sua idade:"))
ingresso = input("Digite se tem o ingresso S/N:")
lista_convidados = input("Digite se está na lista de convidados S/N:")

if (idade >= 18 and ingresso == "S") or lista_convidados == "S":
    print("Acesso Liberado! Aproveite muito o show!")
else:
    print("Acesso negado!")