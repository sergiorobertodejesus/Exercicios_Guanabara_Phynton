soma = quant = media = maior = menor = 0
while True:
    num = int(input("digite um numero : "))
    soma += num 
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar [S N]: ")).upper().strip()[0]
    if resp == "N":
        break
media = soma / quant
print(f'foram digitados {quant} numeros e a media é {media} ')
print(f" e o maior numero foi {maior} e o menor numero foi {menor}")
    