print("\n------TABUADA FIXA------")

numero = int(input("Digite um número para ver a sua tabuada: "))
lista_numeros = [1,2,3,4,5,6,7,8,9]

print(f"A tabuada do número {numero} que foi escolhida!")

for n in lista_numeros:
    tabuada = numero * n
    print(f"{n} x {numero} = {tabuada}")
