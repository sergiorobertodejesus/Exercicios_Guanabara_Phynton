from datetime import date
hoje = date.today().year
ano = int(input(" Ano de Nascimento: "))
nasc = hoje - ano
print(f" O atleta tem {nasc}")

if nasc <= 9:
    print("Classificação: MIRIM")
elif nasc > 9 and nasc <= 14:
    print("Classificação:INFANTIL")
elif nasc > 14 and nasc <= 19:
    print("Classificação: JUNIOR")
elif nasc > 19 and nasc <= 25:
    print("Classificação: SENIOR")
else:
    nasc < 25
    print("Classificação: MASTER")