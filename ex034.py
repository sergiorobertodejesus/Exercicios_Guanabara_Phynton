salario = float(input("qual o seu salario: "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f"quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}")
else:
    salario >= 1250
    novo = salario + (salario * 10 / 100)
    print(f"quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}")