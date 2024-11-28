peso = float(input("Qual seu peso: "))
altura = float(input("qual a sua altura: "))
imc = ( peso / (altura * altura))

print(f"o imc dessa pesso e {imc:.2f}")
if imc < 18.5:
    print("Parabens vc ABAIXO DO PESO")
elif imc >= 18.5 and imc < 24.9:
    print("Seu peso esta NORMAL")
elif imc >= 24.9 and imc < 29.9:
    print("Voçe esta em Sobreso")
elif imc >= 30 and imc < 34.9:
    print("Voçe esta com OBESIDADE GRAU I")
elif imc >= 35 and imc< 39.9:
    print("Voçe esta com OBESIDADE GRAU II")
else:
    imc >= 40
    print("Voçe esta com obesidade GRAU III ou Obsidade MORBIDA")
    
    







