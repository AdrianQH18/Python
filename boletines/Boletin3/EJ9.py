"""
Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
nuestro destino (París, Roma, Santiago de Chile o Tokio)
"""
opcion=input("Cual es su destino: Francia,Italia,Chile o Japón")
match opcion:
    case "Francia":
        print("Capital Paris")
    case "Italia":
        print("Capital Roma")
    case "Chile":
        print("Capital Santiago")
    case "Japon":
        print("Capital Tokio")
    case _:
        print("destino no reconocido")
