print("\n------CONVERSOR DE VELOCIDADE------")

velocidade_km = int(input("\nDigite a velocidade em k/h:"))
velocidade_ms = velocidade_km / 3.6

def converter_km_para_ms (velocidade_km, velocidade_ms):
    if velocidade_km > 80:
        velocidade_ms = velocidade_km / 3.6
        return f"Sua velocidade em m/s é: {velocidade_ms}"
        return "Reduza a Velocidade!"

conversor = converter_km_para_ms(velocidade_km,velocidade_ms)
print(conversor)