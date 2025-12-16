"""
Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas.
"""
nif=input("Introduce un NIF")
if len(nif)==9:
    parteNumerica=nif[:8]
    letra=nif[8]
    if parteNumerica.isdigit() and letra.isdigit():
        print("NIF válido.")
    else:
        print("NIF no valida")
else:
    print("NIF no valido")
