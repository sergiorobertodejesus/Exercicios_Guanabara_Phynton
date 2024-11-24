frase = str(input("digite uma frase: ")).upper().strip()
print(f"a palavra A aparece {frase.count("A")} vezes")
print(f"a palavra A aparece a primeira vez na {frase.find("A")+1}")
print(f"a palavra A aparece pela ultima vez na {frase.rfind("A")+1}")