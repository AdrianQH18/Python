"""
Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos
por pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
que sólo sirve para finalizar el programa)
"""
salir=False
contador=0
while not salir:
    numero=input("Introduce el numero...para finalizar escriba la palabra fin")
    if numero=="FIN":
        print("Entradas validas: ",contador)
        salir = True
    elif int(numero)>100 or int(numero)<1:
        print("Error....")
    elif 1<=int(numero)<=100:
        contador+=1
