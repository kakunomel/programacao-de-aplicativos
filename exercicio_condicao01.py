print("----CLASSIFICADOR DE NOTAS-----")

nota = int(input("Digite uma nota: "))

def avaliar_desempenho (nota):
    if nota >= 9:
        print("Excelente!")
    elif nota >= 7:
        print("Bom!")
    elif nota >5:
        print("Regular!")
    else:
        print("Insuficiente!")

avaliar_desempenho(nota)