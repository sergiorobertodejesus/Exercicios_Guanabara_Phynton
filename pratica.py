print( )
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termo vc quer ver: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}',end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print(f' -> {t3}',end='')