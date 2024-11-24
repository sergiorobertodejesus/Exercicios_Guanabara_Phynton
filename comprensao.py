contador = 0
lista =["azul","amarelo","vermelho","laranja","marron","aZUL","roxo","verde","rosa","Azul"]
lis = [item.upper() for item in lista]
cor = str(input("diga cor: ")).strip().upper()
contador = lis.count(cor)
print(f" a cor {cor} tem {contador} lista")
if contador == 0:
    print(f"a cor {cor} não tem na lista")