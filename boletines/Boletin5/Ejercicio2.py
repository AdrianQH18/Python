# 2. Hacer un programa en que nos permita calcular todos los divisores comunes a dos
# números

input1 = int(input("Ejercicio 2: Añade el primer numero para calcular su division: "))
input2 = int(input("Ejercicio 2: Añade el segundo numero para calcular su division: "))
divisores = []

for i in range(1, min(input1, input2) + 1):
    if input1 % i == 0 and input2 % i == 0:
        divisores.append(i)

print(divisores)