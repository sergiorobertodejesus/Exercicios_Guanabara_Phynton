dias = float(input(' Quantos dias alugados: '))
km = float(input(' Quantos km rodados: '))
total = dias * 60
total2= km * 0.15
print(f'o total a pagar é de R${total+total2:.2f}')

dias = float(input("Quantos dias Alugados: "))
km = float(input("Quantos kms rodados:  "))
diaria = 60
km_rodado = 0.15
total = (dias*diaria)+(km*km_rodado)
print(f"O total a pagar é de R${total:.2f}")