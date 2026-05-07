print("\n------FILTRO APROVADOS------")

alunos = ["Melissa", "Paulo", "Maria", "Arthur", "Eduarda"]
notas = [80, 70, 59, 90, 50]

for nota in notas:
    if nota >= 60:
        indice = notas.index(nota)
        print("Alunos aprovados:" ,alunos[indice])
print(f"Lista dos alunos: {alunos}")