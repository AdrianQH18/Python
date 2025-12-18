import random

# 1 Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
# ninguno de ellos esté repetido (simulando una lotería primitiva).

# Manera facil

randomNumbers = random.sample(range(1, 49), 6)
print(f"randomNumbers Facil: {randomNumbers}")

# Manera normal

randomNumbers = []  # Declaramos una lista vacia

for _ in range(6):
    num = random.randint(1, 49)  # declaramos una variable de numeros aleatorios
    for numeros in randomNumbers:
        num = random.randint(1, 49)
    randomNumbers.append(num)

print(f"randomNumbers Normal: {randomNumbers}")
