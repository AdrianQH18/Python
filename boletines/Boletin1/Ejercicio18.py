"""
Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
un mensaje tétrico (¡Faltan 236 días para que se acabe todox por ejemplo)
"""
import random
contador=0
salir=False
while not salir:
    num=random.randint(1,1000)
    contador+=1
    if num==666:
        salir=True
print("¡Faltan", contador ,"días para que se acabe todox")