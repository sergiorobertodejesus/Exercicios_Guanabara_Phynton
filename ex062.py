primeiro = int(input("\nPrimeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao  # Calcula o último termo da PA
termo_atual = primeiro  # Começa com o primeiro termo
con = False
cont = 0


while termo_atual <= decimo:  # Enquanto o termo atual não ultrapassar o décimo
    print(termo_atual, end=" -> ")
    termo_atual += razao  # Incrementa o termo atual 
    cont += 1
print("Pausa")

while not con:
    pergunta = int(input("Quantos termos voçe quer mostrar a mais: "))
    if pergunta == 0:
        con = True
    else:
        for _ in range(pergunta):
            print(termo_atual,end=" -> ")
            termo_atual += razao
            cont += 1
        print("PAUSA") 
print(f"progressao finalizada com {cont}termos mostrados")


    