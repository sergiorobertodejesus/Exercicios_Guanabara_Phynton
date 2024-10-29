dias = float(input(' Quantos dias alugados: '))
km = float(input(' Quantos km rodados: '))
total = dias * 60
total2= km * 0.15
print(f'o total a pagar é de R${total+total2:.2f}')