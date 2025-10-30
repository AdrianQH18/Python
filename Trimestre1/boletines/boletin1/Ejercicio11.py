#Modificar el programa anterior para que tu programa tire dos dados de forma continuada
#hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
#ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado
import random
salir=False
contador=0
while not salir:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    contador+=1
    if dado1==dado2:
        salir=True

print("En el intento ",contador," Los dados salieron iguales")