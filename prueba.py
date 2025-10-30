import random
contador=0
salir= False
while not salir:
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    if dado1 == dado2:
        print("Dado1: ", dado1)
        print("Dado2: ", dado2)
        salir=True
    contador+=1
print("Dados igualeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees en el intento: ",contador)