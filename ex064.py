num = cont = soma = 0
mult = 1
num = int(input("digite um numero ou [999 para parar]"))
while num != 999:
    soma += num
    mult *= num
    cont += 1
    num = int(input("digite um numero ou [999 para parar]: "))
print(f'foram digitados {cont} numeros que somados dão {soma} e multiplicados dão {mult}')
    