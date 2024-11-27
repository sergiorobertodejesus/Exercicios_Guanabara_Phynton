from datetime import date

# Entrada do ano de nascimento
ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {atual}.")

# Entrada do sexo
sexo = input("Sexo (F ou M): ").strip().upper()

# Verificação do sexo
if sexo == "F":
    print("Não há alistamento obrigatório para mulheres. Obrigado!")
elif sexo == "M":
    # Lógica para alistamento masculino
    if idade == 18:
        print("Você tem que se alistar imediatamente.")
    elif idade < 18:
        saldo = 18 - idade
        print(f"Ainda faltam {saldo} anos para o alistamento.")
        ano1 = atual + saldo
        print(f"Seu alistamento será em {ano1}.")
    else:  # idade > 18
        saldo = idade - 18
        print(f"Você já deveria ter se alistado há {saldo} anos.")
        ano1 = atual - saldo
        print(f"Seu alistamento foi em {ano1}.")
else:
    print("Sexo inválido. Por favor, insira 'F' ou 'M'.")
