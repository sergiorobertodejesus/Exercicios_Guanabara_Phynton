km = float(input("qual é a distancia da sua viagem: "))
preço = 0
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f"Voçe esta prestes a começar uma viagem de {km}KM")
print(f"E o preço de sua passagem sera de R${preço:.2f}")