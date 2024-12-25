from time import sleep
primeiro = int(input("primeiro valor: "))
segundo = int(input("segundo valor: "))
print('''
[ 1 ] somar\n
[ 2 ] multiplicar\n
[ 3 ] maior\n
[ 4 ] novos numeros\n
[ 5 ] sair do programa''')
sair = False
while not sair:
    opçao = int(input("qual a sua opçao: "))
    if opçao == 5:
        sair = True
        print("finalizando...")
        sleep(3)
        print("fim do programa volte sempre")
    else:
        if opçao == 1:
            soma = primeiro + segundo
            print(f"a soma de {primeiro} e {segundo} é {soma} ")  
        elif opçao == 2:
            multi = primeiro * segundo
            print(f"a multiplicaçao de {primeiro} e {segundo} é {multi}")
        elif opçao == 3:
            if primeiro > segundo:
                print(f"o maior entre {primeiro} e {segundo} é {primeiro}.")
            elif segundo > primeiro:
                print(f"o maior entre {primeiro} e {segundo} é o {segundo}")
            else:
                print(f"os dois são iguais {primeiro}")  
        elif opçao == 4:
            print("informe os numeros novamente:")          
            primeiro = int(input("Primeiro valor:"))     
            segundo = int(input("Segundo valor: "))     
        else:
            print('Opção invalida tente novamente')    