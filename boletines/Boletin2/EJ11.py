"""
Modificar el programa anterior para que, además, nos diga al final cual han sido el
número mayor y el menor que has introducido
"""
salir=False
contador=0
acumulador=0
numMayor=None
numMenor=None
while not salir:
    numero=input("Introduce el numero...para finalizar escriba la palabra fin")
    if numero=="FIN":
        salir = True
    elif int(numero)>100 or int(numero)<1:
        print("Error....")
    elif 1<=int(numero)<=100:
        acumulador+=int(numero)
        contador+=1
        if numMenor is None or numMenor>int(numero):
            numMenor=int(numero)
        if numMayor is None or numMayor<int(numero):
            numMayor=int(numero)
mediaAritmeica=acumulador/contador
print("Entradas validas: ",contador)
print("Media de Entradas validas: ",mediaAritmeica)
print("Numero mayor: ",numMayor)
print("Numero menor: ",numMenor)