print("------CALCULADORA DE IMPOSTO------")

salarios = [2000, 2500, 1800, 3150, 1300]

print(f"Observe os salários: {salarios}")

for s in salarios:
    if s <= 2000.00:
        imposto = s * 0.10
        obra = s - imposto
        percentual = "10%"
    elif s > 2000.00:
        imposto = s * 0.20
        sobra = s - imposto
        percentual = "20%"

    print(f"\nO salário {s} foi cobrado {percentual} de imposto") 