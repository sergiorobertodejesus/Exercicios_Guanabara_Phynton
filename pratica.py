primeiro = int(input("\nPrimeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao  # Calcula o último termo da PA
termo_atual = primeiro  # Começa com o primeiro termo
con = False
cont = 0  # Contador de termos exibidos

# Exibindo os 10 primeiros termos
while termo_atual <= decimo:  # Enquanto o termo atual não ultrapassar o décimo
    print(termo_atual, end=" -> ")
    termo_atual += razao  # Incrementa o termo atual pela razão
    cont += 1
print("PAUSA")

# Exibindo termos adicionais
while not con:
    pergunta = int(input("Quantos termos você quer mostrar a mais? "))
    if pergunta == 0:  # Se o usuário não quiser mais termos
        con = True
    else:
        for _ in range(pergunta):  # Exibe os termos adicionais
            print(termo_atual, end=" -> ")
            termo_atual += razao
            cont += 1
        print("PAUSA")

print(f"Progressão finalizada com {cont} termos mostrados.")
