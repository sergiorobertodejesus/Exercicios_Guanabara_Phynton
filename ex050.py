numeros = []
for i in range(1,7):
    dig = int(input("Digite um numero: "))
    numeros.append(dig)
pares = 0
quant = 0

# Loop para verificar e somar apenas os números pares
for num in numeros:
    if num % 2 == 0:  # Verificar se o número é par
        pares += num
        quant += 1

# Exibir o resultado
print(f"vç digitou {quant} pares e a soma dos números pares é: {pares}")
    
    
    
    
