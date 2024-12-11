peso = []
maiores = 0
menores = 0

for i in range(1, 6):
    pes = float(input(f"Peso da {i}ª pessoa: "))
    peso.append(pes)

# Calcular o maior e o menor peso
    if i == 1:
        maiores = pes
        menores = pes
    else:
        if maiores > pes:
            pes = maiores
        if menores < pes:
            pes = menores
    
    
print(f"O maior peso lido foi {maiores}kg")
print(f"O menor peso lido foi {menores}kg")

