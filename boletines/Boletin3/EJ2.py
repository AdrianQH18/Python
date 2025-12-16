"""
Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
informe del número de intentos inválidos
"""
salir=False
contador=0
while not salir:
    contraseña1=input("Introduce la contraseña:")
    contraseña2=input("Introduce la contraseña nuevamente:")
    contador += 1
    if contraseña1!=contraseña2:
        print("Contraseña no coinciden")
    elif contraseña1==contraseña2:
        print("Contraseña confirmada")
        salir=True
print("Numero de intentos: ",contador)