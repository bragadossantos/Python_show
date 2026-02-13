import random

numero_secreto = random.randint(1, 100)
palpite = int(input("Adivinha o número (1 a 100): "))

if palpite == numero_secreto:
    print("Parabéns! Acertaste!")
else:
    print("Erraste... o número era", numero_secreto)