num = cont = soma = 0
mult = 1
while True:
    num = int(input("digite um numero ou [999 para parar]"))
    if num == 999:
        break
    soma += num
    mult *= num
    cont += 1    
print(f'foram digitados {cont} numeros que somados dão {soma} e multiplicados dão {mult}')
    