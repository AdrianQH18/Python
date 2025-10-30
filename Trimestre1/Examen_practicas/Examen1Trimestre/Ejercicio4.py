salir=False
while not salir:
    fraccion = input("Escriba tu fraccion: ")
    lista = fraccion.split("/")
    numerador = lista[0]
    denominador = lista[1]
    if fraccion.count("/") > 1 or fraccion.count("/") < 1:
        print("Error demasiados /")
    elif fraccion[0] == "/" or fraccion[len(fraccion)] == "/":
        print("Error el / no puede ir al inicio o al final")
    elif lista[0].count(".") != 0 or lista[2].count(".") != 0:
        print("El numerador ni el denominador pueden llevar decimales")
    elif lista[1] == "0":
        print("El denominador no puede ser 0")
    elif lista[0].isdigit() != True or lista[1].isdigit() != True:
        print("La fraccion contiene caracteres que no son digitos")
    else:
        fraccionfinal=int(numerador)/int(denominador)
        print(numerador)
        print(denominador)
        print(round(fraccionfinal,3))
        salir=True
    """
    """

