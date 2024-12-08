num = []
for i in range(1,7):
    num2 = int(input("Digite um numero: "))
    num.append(num2)
cont = 0
som = 0
for item in num:
    if item % 2 == 0:
        cont += 1
        som += item
print(f"os {cont} pares somados dão {som}")
