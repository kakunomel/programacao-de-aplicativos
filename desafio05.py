garrafas = int(input("Qual o número total de garrafas que já passaram pela esteira? "))

if garrafas == 500:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")
    print("QUALIDADE: Retire a amostra para teste!")

elif garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")

elif garrafas % 100 == 0:
    print("QUALIDADE: Retire a amostra para teste!")

else:
    print(f"Produção em dia. Garrafa número {garrafas} processada.")