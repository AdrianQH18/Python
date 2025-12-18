# 5. Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y
# 50 (ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces
# se repite (y nos diga cuantas veces lo hace).

import random

randomNumbers = random.sample(range(1, 50), 30)  # Genera valores entre el 1 y 50, 100 veces variables
maximo = max(randomNumbers)  # Sacar numero maximo de la lista
minimo = min(randomNumbers)  # Sacar numero minimo de la lista
veces_repetidas = list(randomNumbers)  # Convertimos veces_repetidas a una lista
for i in range(1, 100):
    veces_repetidas.count(i)  # Sacar el numero mas repetido

print(f"""El valor maximo es: {maximo} el valor minimo es: {minimo} 
      \t el valor que se repite mas veces {veces_repetidas}""")
