# importar a biblioteca pygame
from pygame import mixer

# uma forma de implementar o código
mixer.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
mixer.music.load('KillBill.mp3')
mixer.music.play()
x = input('Digite algo para parar...')