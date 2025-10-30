"""
Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
8, 12, etc.) A continuación debería de hacer la tirada y mostrarla
"""
import random
numDados=int(input("Introduce el numero de dados que vas a lanzar"))
numCaras=int(input("Introduce el numero de caras de los dados"))

for i in range(numDados):
    valorDado=random.randint(1,numCaras)
    print("El dado ",i,": ",valorDado)