num = int(input("informe um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''
Analizando o numero {num}\n 
sua unidade {u}\n
sua dezena {d}\n
sua centena {c}\n
seua milhar {m}    
      ''')