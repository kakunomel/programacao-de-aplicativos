print("------BATALHA RPG------")

vida_inicial = 100
valor_dano = 0

def sofrer_dano(vida_inicial, valor_dano):
    while vida_inicial != 0:
        valor_dano = int(input("Digite o valor do dano que o monstro causou: "))
        vida_inicial = vida_inicial - valor_dano
        print(f"Saldo de vida atualizada: {vida_inicial}") 
    print("Game Over!")

sofrer_dano(vida_inicial, valor_dano)