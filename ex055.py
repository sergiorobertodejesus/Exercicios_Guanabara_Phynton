
peso = []
maiores = 0
menores = 0


for i in range(1,6):
    pes = int(input(f"Peso da {i}º pessoa: "))
    peso.append(pes)
    
maiores = max(peso)  
menores = min(peso)
  

 
print(f"O maior peso lido foi {maiores}kg")
print(f"O menor peso lido foi {menores}kg")