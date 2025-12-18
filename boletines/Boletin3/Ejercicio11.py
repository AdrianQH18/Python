# 11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
# comunique, además de si es válido de que tipo es.Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
# continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
# escritas con mayúsculas o con minúsculas

dni = str(input("Ejercicio 11: Introduzca un NIF o NIE español: "))

numeros = dni[:8]
letra = dni[-1]

if len(dni) == 9:
    if numeros.isdigit() and letra.isalpha():
        print(f"El DNI es valido: {dni}")
    else:
        print(f"El DNI no es valido: {dni}")
else:
    print("No tiene 9 caracteres")