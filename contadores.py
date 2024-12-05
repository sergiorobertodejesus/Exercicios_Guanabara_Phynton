
cont = 0
lista = ["azul","amarelo","vermelho","azul","bege","amarelo","azul"]
for item in lista:
    if item == "preto":
        cont += 1
print(f" A Palavra 'azul' aparece {cont} vezes")
for i in range(1,10):
    cont += i
    print(cont)

    