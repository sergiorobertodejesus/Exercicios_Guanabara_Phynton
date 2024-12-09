frase = str(input("Qual a frase: "))
frase2 = frase.replace(" ","")
invertida = frase2[::-1]
if frase2 == invertida:
    print(f"A frase {frase} é um palindromo")
else:
    print(f"A frase {frase} nao e um palindromo")
