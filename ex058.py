import random,time
print('-=' *20)
print('''Sou seu computador ...\n
      Acabei de pensar em um numero entre 0 e 10.\n
      Sera que vc consegue adivinhar qual foi ''')
print('-=' *20)
numero = random.randint(1,11)
eu = None
while True:
    eu = int(input("Qual seu palpite: "))
    if eu == -1:
        print("\033[0;31;46mate logo\033[m")
        break
    else:
        print("PROCESSANDO....")
        time.sleep(3)
        if numero == eu:
            print(f"Voçe acertou! voçe ganhou")
        else:
            print(f"GANHEI! Eu pensei no numero {numero} e não no {eu}")



