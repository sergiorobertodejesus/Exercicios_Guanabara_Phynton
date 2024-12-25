from random import randint
computador = randint(0,10)
print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 e 10.")
print("Sera que consegue adivinhar qual foi: ")
acerto = False
tentativa = 0
while not acerto:
    palpite = int(input("Qual seu palpite: "))
    tentativa += 1
    if palpite == computador:
        acerto = True
    else:
        if palpite < computador:
            print("Mais...! tente outra vez")
        elif palpite > computador:
            print("Menos...!tente outra vez")
            
print(f"Voçe acertou com {tentativa} parabens")