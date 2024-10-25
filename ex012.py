preço = float(input(' Qual preço do produto:R$ '))
desc = preço*5/100
final = preço - desc
print(f'o produto que custava R${preço},na promoção com desconto de 5% vai custar R${final:.2f}')