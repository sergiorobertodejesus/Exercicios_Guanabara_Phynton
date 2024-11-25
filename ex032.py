from datetime import date

ano = int(input("Que ano quer analisar coloque 0 para analizar ano atual: "))
atual = date.today().year
if ano == 0:
    if(atual % 4 == 0 and atual % 100 != 0) or atual % 400 == 0:
        print("ano bissexto")
    else:
        print('Não é um ano bissexto. ')
        
        
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto. ')
    
else:
    print('Não é um ano bissexto. ')