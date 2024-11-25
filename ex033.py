primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
terceiro = int(input("terceiro valor: "))
menor= 0
maior = 0
if primeiro < segundo and primeiro < terceiro:
    print(f"menor é {primeiro}")
elif segundo < primeiro and segundo < terceiro:
    print(f'menor é {segundo}')
elif terceiro < segundo and terceiro < primeiro:
    print(f"o menor  {terceiro}")
if primeiro > segundo and primeiro > terceiro:
    print(f"maior é {primeiro}")
elif segundo > primeiro and primeiro > terceiro:
    print(f"maior é o {segundo}")
elif terceiro >primeiro and terceiro > segundo:
    print(f"maior é {terceiro}")

    
