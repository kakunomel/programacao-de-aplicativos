print("\n------CONVERSOR DE VELOCIDADE------")

velocidade_km = int(input("\nDigite a velocidade em k/h:"))
velocidade_ms = velocidade_km / 3.6

def converter_km_para_ms (velocidade_km, velocidade_ms):
    velocidade_ms = velocidade_km / 3.6
    if velocidade_km > 80:
        print("Reduza a Velocidade!")
        return f"Sua velocidade em m/s é: {velocidade_ms}"
    return f"Sua velocidade em m/s é: {velocidade_ms}"

conversor = converter_km_para_ms(velocidade_km,velocidade_ms)
print(conversor)