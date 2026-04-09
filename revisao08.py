print("\n--------CALCULADORA IMC--------")

peso = float(input("\nNos informe o seu peso: "))
altura = float(input("Nos infome a sua altura: "))
calculo = peso / (altura * 2)

if calculo > 25:
    print("\nSeu IMC é " , calculo)
    print("Você está com sobrepeso!")
else:
    print("\nSeu IMC é " , calculo)
    print("Seu peso está normal!")