somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho= ''
totmulher20 = 0

for i in range(1,5):
    print(f"-----{i} pessoa-----")
    nome = str(input("nome: ")).strip()
    idade = int(input("idade: "))
    sexo = str(input("sexo [M\F]: ")).strip()
    somaidade += idade
    if i == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f"a media de idade do grupo e de {mediaidade}")                
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")                
print(f"ao todo sao  {totmulher20} mulheres com menos de 20 anos")                