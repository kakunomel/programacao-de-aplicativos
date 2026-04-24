print("------LOCALIZADOR ITENS------")

nomes = ["banana", "maçã", "laranja", "mamão", "manga", "açaí", "melancia", "tangerina", "abacaxi", "uva"]
buscar_nome = input("Digite o nome da fruta que está procurando: ")

def esta_na_lista(nomes, buscar_nome):
    for n in nomes:
        if n == buscar_nome:
            return "Encontrado!"
    return "Não disponível!"

msg = esta_na_lista(nomes, buscar_nome)
print(msg)
