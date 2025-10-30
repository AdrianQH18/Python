frase=input("Introduce una frase: ")
letra=input("Letra a mantener: ")
cadenafinal=""
contador=0
intentos=0
salir=False
while not salir:
    nuevaLetra = input("Introduce una letra")
    nuevaCadena = ""
    for i in frase:
        if i == letra or i == nuevaLetra:
            nuevaCadena+=i
            if i == nuevaLetra:
                contador += 1
        else:
            if i == " ":
                nuevaCadena +=" "
            else:
                nuevaCadena+="*"
    cadenafinal=nuevaCadena
    print(nuevaCadena)
    print("\nla letra ", nuevaLetra, " aparece en ", contador, " ocasiones")