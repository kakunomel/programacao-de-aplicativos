media = float(input("Digite a sua média escolar:"))
renda = float(input("Digite a sua renda familiar:"))
escola_publica = input("Digite se veio de escola pública S/N:")

if (media >= 8.0 and renda <= 2000.00) or escola_publica == "S":
    print("Parabéns! Você ganhou uma bolsa!")
else:
    print("Infelizmente você não conseguiu uma bolsa.")
    