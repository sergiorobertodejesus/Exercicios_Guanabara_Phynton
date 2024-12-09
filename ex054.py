from datetime import datetime
anos = []
maiores = 0
menores = 0
ano_atual = datetime.now().year

for i in range(1,8):
    ano = int(input(f"E que ano a {i}º pessoa nasceu: "))
    anos.append(ano)
    idade = ano_atual - ano

    if idade >= 18:
        maiores += 1        
    else:
        menores += 1
print(f"Tivemos {maiores} pessoas maiores de idade" )
print(f"E tambem tivemos {menores} pessoas menores de idade")