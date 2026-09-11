numeros = list(range(1, 101))

def busca_sequencial():
    procurado = 95
    encontrado = False

    for n in range(len(numeros)):
        if numeros[n] == procurado:
            print(f"Valor encontrado na posição {n}")
            encontrado = True
            break

    else:
        print("Valor não encontrado")


def busca_binária():
    procurado = 95
    inicio = 0
    fim = len(numeros) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if numeros[meio] == procurado:
            posicao = meio
            inicio = fim + 1

        elif numeros[meio] < procurado:
            inicio = meio + 1

        else:
            fim = meio - 1

    if posicao != -1:
        print("Valor encontrado na posição:", posicao)
    else:
        print("Valor não encontrado")

busca_sequencial()