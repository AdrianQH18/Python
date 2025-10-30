#Modificar el programa del punto anterior para que si el primer número que metemos es
#mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
#en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
#50 y el 10 que no tiene mucha lógica…)
import random
salir=False
while not salir:
    num1=int(input("Introduzca el primer numero: "))
    num2=int(input("Introduzca el segundo numero: "))
    if num1>num2:
        numRandom=random.randint(num2,num1)
        print("Numero aleatorio es: ", numRandom)
        salir=True
    else:
        print("El primer numero tiene que ser mayor que el segundo introducido")

"""
if num1>num2:
    numAleatorio=random.randint(num2,num1)
    print("Numero aleatorio es: ", numAleatorio)
else:
    print("El primer numero tiene que ser mayor:")
"""
