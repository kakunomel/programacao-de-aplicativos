print("---- ESTUFA INTELIGENTE ----")
temperatura = float(input("Qual a temperatura da estufa? "))

if temperatura <= 30:
    print("CLIMA ESTÁVEL!")
else:
    print("ALERTA DE CALOR!")

print("----------------------------")

umidade = float(input("Digite a umidade da estufa "))

if umidade <= 40:
    print("AÇÃO: LIGAR A IRRIGAÇÃO!")
else:
    print("AÇÃO: LIGAR APENAS VENTILADORES.")