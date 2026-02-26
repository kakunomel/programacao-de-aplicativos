media = float(input("Digite sua média final:"))
presenca = int(input("Digite a porcentagem da sua presença:"))

if media >= 7.0 and presenca >= 75:
    print("Parabéns! Você foi aprovado.")
elif media < 7.0 and presenca < 75:
    print("Reprovado. Verifique sua nota ou frequência.")
elif media >= 7.0 and presenca < 75:
    print("Reprovado. Verifique sua nota ou frequência.")
elif media < 7.0 and presenca >= 75:
    print("Reprovado. Verifique sua nota ou frequência.")
    