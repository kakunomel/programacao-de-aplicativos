codigo = int(input("Qual o código do Drone? "))
autorização = input("O Drone possui autorização para pousar? ")

if codigo == 999 or autorização == "S":
    print("POUSO AUTORIZADO!")

    print("----------------------------")

    bateria = int(input("Qual a bateria do Drone? "))
    clima = input("Qual o clima do dia? ")
    vento = int(input("Qual a velocidade do vento em KM? "))

    if bateria < 10:
        print("POUSO AUTORIZADO. POUSE IMEDIATAMENTE!")

    elif bateria >=10:
        if (clima == "Ensolarado" and vento < 30) or (clima == "Chuvoso" and vento < 10):
                print("POUSO AUTORIZADO: Iniciando descida.")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")
else:
    print("ERRO 01: Drone não identificado. Retornando à base.")

