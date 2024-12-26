n = int(input("Digite um numero para caucular seu fatorial: "))
c = n
f = 1
print(f"calculando fatorial de {n} ! ",end='')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')    

n = int(input("Digite um numero para calcular seu fatorial: "))
f = 1
print(f"calculando fatorial de {n} ! ",end='')
for c in range(n,0,-1):
    print(f'{c}', end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
print(f"{f}")    
    
    

