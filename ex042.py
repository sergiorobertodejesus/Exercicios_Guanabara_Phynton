print("-=" *20)
print("analisador de triangulos")
print("=-" *20)
r1 = float(input("primeiro segmento: "))
r2 = float(input("segundo segmento: "))
r3 = float(input("terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triangulo")
    if r1 == r2 == r3 :
        print("os segmentos formam triangulo equilatero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Os segmentos formam um triângulo isósceles.")
    else:
        print("Os segmentos formam um triângulo escaleno.")
else:
    print("os segmentos acima não podem formar um triangulo")