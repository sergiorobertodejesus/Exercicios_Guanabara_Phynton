produto = float(input("preço das compras: "))
print('''
FORMAS DE PAGAMENTO \n
[ 1 ] á vista dinheiro\cheque \n
[ 2 ] á vista cartão \n
[ 3 ] 2x no cartão \n
[ 4 ] 3x ou mais no cartão ''')
opção = int(input("Qual é a opção: "))
um = produto - (produto * 10 / 100) 
dois = produto - (produto * 5 / 100) 
if opção == 1:
    print(f"Sua compra de R${opção} vai custar {um}")
elif opção == 2:
     print(f"Sua compra de R${produto} vai custar {dois}")
elif opção == 3:
    cartao = int(input("Em 1 para uma vez,ou 2 para duas vezes: "))
    if cartao == 1:
        print(f"o valor no cartao em uma vez sera de {produto}")
    else:
        print(f"Sua compra de R${produto} vai custar 2 x {produto/2}")
elif opção == 4:
    quatrox = int(input("quantas vezes: "))
    quatro = produto + (produto * 20 / 100) 
    if quatrox >= 3:
        print(f"Sua compra de R${produto:.2f} vai custar {quatrox}x  de {quatro/quatrox:.2f}")
    
    
