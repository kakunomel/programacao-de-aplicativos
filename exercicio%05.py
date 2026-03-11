print("--------DIVISÃO DE CARGAS--------")

codigo_pacote = int(input("Qual o código do pacote? "))
peso = float(input("Qual o peso do pacote? "))

print("---------------------------------")

if peso < 5 and (codigo_pacote % 10 == 0):
    print(f"Pacote {codigo_pacote}: ENTREGA EXPRESSA")
elif peso > 50:
    print(f"Pacote {codigo_pacote}: CARGA PESADA")
else:
    print("INFORMAÇÕES INVÁLIDAS!")