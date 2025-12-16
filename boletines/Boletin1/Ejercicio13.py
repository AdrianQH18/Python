"""
Modifica el programa anterior para que no admita dados con un número de caras impares
(¡no existen!). En el caso de meter un número impar de caras el programa debería de
informarnos de que es erróneo y volver a preguntarnos por este dato
"""
import random
salir=False
while not salir:
    numDados=int(input("Introduce el numero de dados que vas a lanzar"))
    numCaras=int(input("Introduce el numero de caras de los dados"))
    if numCaras%2==0:
        for i in range(numDados):
            valorDado=random.randint(1,numCaras)
            print("El dado ",i,": ",valorDado)
        salir=True
    else:
        print("!!!!!!!!!!ERROR!!!!!!!!!!")
        print("El numero de caras tiene que ser par")
