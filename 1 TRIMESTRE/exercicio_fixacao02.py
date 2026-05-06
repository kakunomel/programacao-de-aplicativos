pendentes = ["Relatório.pdf", "Foto.png", "Planilha.xlsx"]
print(f"Lista de Pendentes {pendentes}")
concluidos = []
print(f"Lista de Concluídos {concluidos}")

print("____________________________________________________")
print("                                                    ")

concluidos.append(pendentes[0])
pendentes.pop(0)

print("Pendentes: ", pendentes)
print("Concluídos: ", concluidos)