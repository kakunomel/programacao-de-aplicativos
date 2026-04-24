print("------APLICADOR DE DESCONTO------")

list_precos =  [150.0, 80.0, 200.0, 50.0] 
list_precos2 = []

def aplicar_promocao(lista, listan):
    for item in lista:
        if item >= 100.00:
            desconto = item * 0.15
            novo_valor = item - desconto
            listan.append(novo_valor)
    print(list_precos2)

aplicar_promocao(list_precos, list_precos2)