cargo = str(input("Digite o seu cargo: "))
codigo = int(input("Digite o seu código: "))
botao_pressionado = input("Botão de emergência pressionado? Digite S ou N: ")
equipamento_completo = input("EPI completo? Digite S ou N: ")

if (cargo == "Engenheiro" or cargo == "Tecnico") and (codigo == 1234 or botao_pressionado == "S") and equipamento_completo == "S":
    print("ACESSO LIBERADO!")
else:
    print("ACESSO NEGADO: RISCO DE SEGURANÇA!")