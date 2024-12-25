from random import randint
computador = randint(0,10)
print('''
Sou seu computador...\n
Acabei de pensar em um numero de 0 a 10.\n
Sera que voçe consegue adivinhar qual foi:''')
tentativa = 0
acerto = False
while not acerto:
    palpite= int(input("Qual seu palpite: "))
    tentativa += 1
    if palpite == computador:
        acerto = True
    else:
        if palpite < computador:
            print("mais...!tente outra vez")
        elif palpite > computador:
            print("mais...! tente outra vez")
print(f"voce acertou com {tentativa} tentativas") 

