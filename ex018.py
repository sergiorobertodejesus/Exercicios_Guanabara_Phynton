import math
angulo =int(input("Digite o angulo que vc deseja: "))
rad = math.radians(angulo)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)
print(f"O angulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O angulo de {angulo} tem o COSENO de {coseno:.2f}")
print(f"O angulo de {angulo} tem o TANGENTE de {tangente:.2f}")


