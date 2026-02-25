salario = float(input("Quanto você recebe:"))

if salario >= 10.000:
    print("Rico")
elif salario >= 5.000:
    print("Classe Média")
elif salario < 5.000:
    print("Classe Baixa")