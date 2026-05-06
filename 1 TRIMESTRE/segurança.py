print("--- OPERADOR DE PRENSA HIDRÁULICA ---")
curso = input("Você concluiu o curso de segurança? ")

if curso == "S":
    instrutor = input("O instrutor está na sala? ")
    if instrutor == "S":
        print("Acesso liberado: Operação iniciada.")
    else:
        print("Aguarde o instrutor para ligar a máquina.")
else:
    print("Acesso negado! Faça o treinamento primeiro.")
