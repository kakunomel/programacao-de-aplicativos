temperaturas = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]

for temperatura in temperaturas:
    print(f"Observe as seguintes temperaturas: {temperatura}")

    if temperatura > 30.0:
        print(f"ALERTA: TEMPERATURA CRÍTICA. {temperatura}°C")
    else:
        print(f"Temperatura Normal. {temperatura}°C")  