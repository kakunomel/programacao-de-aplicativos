print("------MÉDIA DE ALUNO------")

print("\nDigite 4 notas de uma matéria de sua preferência para calcular a média final")

notas = []
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

notas.append(nota1)
notas.append(nota2)
notas.append(nota3)
notas.append(nota4)


for nota in notas:
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print(f"Parabéns!Você foi aprovado.")
    elif media >= 5 and media <= 6.9:
        print(f"Você está de recuperação!")
    else:
        print(f"Você foi reprovado!")
