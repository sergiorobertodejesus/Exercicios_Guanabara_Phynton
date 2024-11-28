print("-=" * 20)
print("Analisador de Triângulos")
print("=-" * 20)

# Entrada dos segmentos
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# Verificar se os segmentos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo.")

    # Verificar o tipo de triângulo
    if r1 == r2 == r3:
        print("Os segmentos formam um triângulo equilátero.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Os segmentos formam um triângulo isósceles.")
    else:
        print("Os segmentos formam um triângulo escaleno.")
else:
    print("Os segmentos acima não podem formar um triângulo.")
