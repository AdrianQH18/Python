"""
Modificar el programa anterior para que nos muestre al final la media aritmética de
las entradas válidas
"""
salir=False
contador=0
acumulador=0
while not salir:
    numero=input("Introduce el numero...para finalizar escriba la palabra fin")
    if numero=="FIN":
        salir = True
    elif int(numero)>100 or int(numero)<1:
        print("Error....")
    elif 1<=int(numero)<=100:
        acumulador+=int(numero)
        contador+=1

mediaAritmeica=acumulador/contador
print("Entradas validas: ",contador)
print("Media de Entradas validas: ",mediaAritmeica)