print("\n SISTEMA DE CHECKOUT COM IMPOSTO E DESCONTO ")

valor_base = int(input("\nDigite o valor base: "))
imposto_percentual = int(input("Digite o valor do imposto: "))
cupom_desconto = int(input("Digite o valor do cupom: "))

def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    subtracao1 = valor_base - imposto_percentual
    valor_total = subtracao1 - cupom_desconto
    if cupom_desconto > valor_base:
        return  0

resultado = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)
print(resultado)