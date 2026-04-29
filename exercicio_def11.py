print("\n SISTEMA DE CHECKOUT COM IMPOSTO E DESCONTO ")

valor_base = int(input("\nDigite o valor base: "))
imposto_percentual = int(input("Digite o valor do imposto: "))
cupom_desconto = int(input("Digite o valor do cupom: "))

def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    soma = valor_base + imposto_percentual
    subtrcao = soma - cupom_desconto
    if cupom_desconto > valor_base:
        print(0)

#CORRIGIR