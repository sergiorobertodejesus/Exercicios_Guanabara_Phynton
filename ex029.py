velocidade = float(input("Qual é a velocidade atual do carro: "))
multa = (velocidade - 80) * 7
if multa >80:
    print(f"\033[31mmultado! voçe excedeu limite permitido que é 80km sua multa é de\033[m \033[33;40mR${multa:.2f}")
print("\033[30;40mtenha um bom dia dirija com segurança\033[m]")      