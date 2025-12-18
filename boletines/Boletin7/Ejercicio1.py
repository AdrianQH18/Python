# Vamos a hacer una pequeña calculadora. Solicita dos números al usuario y luego que
# escriba la operación que quiere hacer (S para suma, R para resta, M para multiplicar y D
# para dividir). Realiza la operación con un switch

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
op = input("Operación (S/R/M/D): ").upper()

match op:
    case "S":
        print("Resultado:", num1 + num2)
    case "R":
        print("Resultado:", num1 - num2)
    case "M":
        print("Resultado:", num1 * num2)
    case "D":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: división por cero")
    case _:
        print("Operación no válida")
