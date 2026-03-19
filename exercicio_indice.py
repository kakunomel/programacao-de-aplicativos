usuario = int(input("Digite o número de uma vaga. Tem que ser de 0 a 3: "))
vagas = ["Livre" , "Ocupado" , "Livre" , "Ocupado"]

if usuario  % 2 == 0 and vagas[usuario] == "Livre":
    print(f"Vaga {usuario} autorizada para estacionar.") 
else:
    print(f"Vaga {usuario} indisponível ou fora das regras.")
    