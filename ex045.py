from random import randint
import time
itens = ("Pedra","Papel","Tesoura")
comp = randint(0,2)
print('''Suas opções:\n
      [ 0 ] PEDRA\n
      [ 1 ] PAPEL\n
      [ 2 ] TESOURA''')
jogada = int(input("Qual a sua jogada: "))
print("JO")
print("KEN")
time.sleep(2)
print("PO!!!")
print("-=" * 20)
print(f"O computador escolheu {itens[comp]}")
print(f"O jogador jogou {itens[jogada]}")
print("-=" * 20)
if comp == 0:
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("JOGADOR VENCE")
    elif jogada == 2:
        print("COMPUTADOR VENCE")
    else:
        print("jogada invalida")
    
elif comp == 1:
    if jogada == 0:
        print("COMPUTADOR VENCE")
    elif jogada == 1:
        print("EMPATE")        
    elif jogada == 2:
        print("JOGADOR VENCE")               
    else:
        print("jogada invalida")    
elif comp == 2:
    if jogada == 0:
        print("JOGADOR VENCE")      
    elif jogada == 1:
        print("COMPUTADOR VENCE")      
     
    elif jogada == 2:
        print("EMPATE")        
    else:
        print("jogada invalida")
        
