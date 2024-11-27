nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda Nota: "))
media = (nota1 + nota2) / 2
print(f" Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno é {media:.1f}")
if media < 5:
    print("O aluno esta reprovado")
elif media >= 5 and media <= 6.9:
    print(f"aluno em recuperaçao")
else:
    media >= 7
    print("o aluno esta aprovado")
