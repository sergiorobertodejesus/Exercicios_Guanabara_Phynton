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
    