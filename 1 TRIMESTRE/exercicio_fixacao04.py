cidades = ["São Paulo", "Rio de janeiro", "Curitiba", "Belo Horizonte"]
nome_cidade = input("Digite o nome de uma cidade: ")

if nome_cidade in cidades:
    posicao = cidades.index(nome_cidade)
    print(f"A cidade {nome_cidade} está na posição {posicao}")
else:
    print("ERRO")