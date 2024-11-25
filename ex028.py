import random,time
print('-=' *20)
print("vou pensar em um numero entre 0 e 5. tente adivinhar")
print('-=' *20)
numero = random.randint(1,5)
eu = None
while True:
    eu = int(input(" Em que numero eu pensei, ou -1 pra sair :  "))
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



