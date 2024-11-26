numero = int(input("Digite um numero inteiro: "))
print('''
Escolha uma das bases para conversão:\n 
[ 1 ] converter para BINARIO\n
[ 2 ] converter para OCTAL\n
[ 3 ] converter para HEXADECIMAL
''')
opção = int(input("Sua opção: "))
if opção == 1:
   binario = bin(numero)[2:]
   print(f"o numero {numero} convertido pra BINARIO é {binario}")
elif opção == 2:
    octal = oct(numero)[2:]
    print(f"o numero {numero} convertido para OCTAL é {octal}")
elif opção == 3:
    hexa = hex(numero)[2:].upper()
    print(f"o numero {numero} convertido para HEXADECIMAL é {hexa}")
else:
    print("digite 1,2,3")