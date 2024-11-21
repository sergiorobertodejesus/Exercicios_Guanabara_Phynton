cateto_oposto = float(input("comprimento do cateto oposto: "))
cateto_adjacente = float(input("comprimento do cateto adjacente: "))
c_o = cateto_oposto **2
c_a = cateto_adjacente **2
h = c_o + c_a
h2 = h **(1/2)
print(f"a hipotenusa vai medir {h2:.2f}")