from time import sleep

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
sair = False

while not sair:
    print('''\nEscolha uma das opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opçao = int(input("Qual a sua opção? "))

    if opçao == 1:
        soma = primeiro + segundo
        print(f"A soma de {primeiro} e {segundo} é {soma}.")
    elif opçao == 2:
        multi = primeiro * segundo
        print(f"A multiplicação de {primeiro} e {segundo} é {multi}.")
    elif opçao == 3:
        if primeiro > segundo:
            print(f"O maior entre {primeiro} e {segundo} é {primeiro}.")
        elif segundo > primeiro:
            print(f"O maior entre {primeiro} e {segundo} é {segundo}.")
        else:
            print(f"Os dois números são iguais: {primeiro}.")
    elif opçao == 4:
        print("Informe os números novamente:")
        primeiro = int(input("Primeiro valor: "))
        segundo = int(input("Segundo valor: "))
    elif opçao == 5:
        sair = True
        print("Finalizando...")
        sleep(2)
        print("Fim do programa. Volte sempre!")
    else:
        print("Opção inválida! Tente novamente.")
