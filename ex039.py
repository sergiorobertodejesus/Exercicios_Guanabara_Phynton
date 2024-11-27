from datetime import date
ano = int(input(" Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"quem nasceu em {ano} tem {idade} em {atual}")
sexo = str(input(" Sexo F & M: ")).strip().upper()
if sexo == "F":
    print("Não ha alistamento feminino, obrigado")
elif sexo =="M":
    if idade == 18:
        print("Voçe tem que se alistar imediatamente")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Ainda faltam {saldo} anos para alistamento")
        ano1 = atual + saldo
        print(f"seu alistamento sera em {ano1}")
    else:
        saldo = idade - 18
        print(f"voce ja deveria ter se alistado a {saldo} anos")
        ano1 = atual - saldo
        print(f" seu alistamento foi em {ano1}")
else:
    print("Sexo invalido insira 'F' ou 'M' ")