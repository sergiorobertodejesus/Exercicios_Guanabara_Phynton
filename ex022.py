nome = str(input("Digite seu nome: ")).strip()
print("Analizando seu nome...")
print(f"Seu nome em Maiusculas é {nome.upper()}") 
print(f"Seu nome em Minusculas é {nome.lower()}") 
print(f"Seu nome tem {len(nome)- nome.count(' ')}")
print(f"Seu primeiro nome tem {nome.find(' ')}")
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]}")
     
      
      
      
      
      
