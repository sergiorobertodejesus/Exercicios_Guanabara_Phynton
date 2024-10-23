largura = float(input('Largura da parede: '))
altura = float(input('altura da parede'))
area = largura * altura
tinta = area / 2
print(f'''
      sua parede tem a dimensão de {altura}x{largura} e sua area e de {area:.2f}\n
      para pintar essa parede voçe precisara de {tinta:.2f}l de tinta
      ''')