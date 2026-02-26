nivel = int(input("Digite o nível em que está: "))
esferas = int(input("Digite a quantidade de esferas coletadas:"))

if nivel >= 20 and esferas >= 50:
    print("Habilidade Super Salto desbloqueada!")
elif nivel < 20 and esferas < 50:
    print("Requisitos insuficientes para nova habilidade!")
elif nivel >= 20 and esferas < 50:
    print("Requisitos insuficientes para nova habilidade!")
elif nivel < 20 and esferas >= 50:
    print("Requisitos insuficientes para nova habilidade!")