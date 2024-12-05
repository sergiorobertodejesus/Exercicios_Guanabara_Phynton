# Criar uma lista vazia fora do loop
numeros = []

# Loop para solicitar 6 números
for i in range(1, 7):
    dig = int(input("Digite um número: "))
    numeros.append(dig)  # Adicionar o número digitado na lista

# Exibir a lista completa
print(numeros)
