while True:
    sexo = input("Informe seu sexo [M/F]: ").strip().upper()
    if sexo in ["M", "F"]:
        print(f"Sexo {sexo} registrado com sucesso.")
        break
    else:
        print("Dados inválidos. Por favor, informe seu sexo corretamente.")
