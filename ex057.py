while True:
    sexo = input("informe seu sexo:[M/F] ").upper().strip()
    if sexo in ["M","F"]:
        print(f"Sexo {sexo} registrado com sucesso")
        break
    else:
        print("Dados invalidos,Por favor,informe seu sexo: ")
        
        
sex = str(input("Digite seu sexo [F/M]")).strip().upper()
while sex not in "MF":
    sex = str(input("Dados invalidos,Por favor,informe seu sexo: ")).strip().upper()
print(f"Sexo {sex} registrado com sucesso")   