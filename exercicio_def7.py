print("\n------CALCULAR ÁREA------")

largura = int(input("Digite a largura do local: "))
comprimento = int(input("Digite o comprimentodo local: "))
area = largura * comprimento
contador = 0

def calcular_area (largura,comprimento):
    while contador != 3:
        largura = int(input("Digite a largura do local: "))
        comprimento = int(input("Digite o comprimentodo local: "))
        area = largura * comprimento
        print(f"A área do terreno é: {area}")

calcular_area(largura,comprimento) 