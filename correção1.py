cont = 0
lista = ["azul", "amarelo", "vermelho", "azul", "bege", "amarelo", "azul"]

for item in lista:  # Itera sobre os itens da lista
    if item == "azul":  # Verifica se o item é "azul"
        cont += 1  # Incrementa o contador

print(f"A palavra 'azul' aparece {cont} vezes.")
