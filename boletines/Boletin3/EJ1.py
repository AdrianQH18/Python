"""
Escribir un programa que pida una contraseña por teclado (dos veces) y si no
coinciden nos lo vuelva a pedir hasta que lo hagan
"""
salir=False
while not salir:
    contraseña1=input("Introduce la contraseña:")
    contraseña2=input("Introduce la contraseña nuevamente:")
    if contraseña1!=contraseña2:
        print("Contraseña no coinciden")
    elif contraseña1==contraseña2:
        print("Contraseña confirmada")
        salir=True