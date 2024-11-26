casa = float(input("Qual valor da casa: "))
salario = float(input("Qual salario: "))
anos = int(input("Quantos anos de finaciamento: "))
ano = anos * 12
prestação = casa / ano
sal = salario * 30 /100
print(f"para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de {prestação:.2f}")
if sal > prestação:
    print("Emprestimo concedido")
else:
    print("Emprestimo negado")