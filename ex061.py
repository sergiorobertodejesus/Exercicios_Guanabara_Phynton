print(          "-=" *20)
print("      OS 10 TERMOS DE UMA PA")
print("=-" *20)
t1 = int(input("Digite o primeiro termo: "))
t2 = int(input("Razão: "))
for i in range(10):  # Vai de 0 a 9 (10 repetições)
    termo = t1 + i * t2  # Fórmula do n-ésimo termo da PA
    print(termo, end=" -> ")

print("FIM")

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
decimo = primeiro+(10 -1) * razão
for c in range(primeiro,decimo + razão, razão):
    print(c,end="-> ")
    
print("-=" * 20)
print("      OS 10 TERMOS DE UMA PA")
print("=-" * 20)

# Primeira parte do código
t1 = int(input("Digite o primeiro termo: "))
t2 = int(input("Razão: "))
contador = 0  # Inicializa o contador
while contador < 10:  # Enquanto o contador for menor que 10
    termo = t1 + contador * t2  # Fórmula do n-ésimo termo da PA
    print(termo, end=" -> ")
    contador += 1  # Incrementa o contador

print("FIM")

# Segunda parte do código
primeiro = int(input("\nPrimeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao  # Calcula o último termo da PA
termo_atual = primeiro  # Começa com o primeiro termo

while termo_atual <= decimo:  # Enquanto o termo atual não ultrapassar o décimo
    print(termo_atual, end=" -> ")
    termo_atual += razao  # Incrementa o termo atual pela razão

print("FIM")

    