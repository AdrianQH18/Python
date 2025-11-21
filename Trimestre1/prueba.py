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

"""
isinstance(obj, tipo) es una función de Python que verifica si un objeto es de un tipo (o de una tupla de tipos) específico.
isinstance(5, int)          # True
isinstance("hola", str)     # True
isinstance(3.14, float)     # True
isinstance([1,2,3], list)   # True
"""