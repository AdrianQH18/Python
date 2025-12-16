"""
7. Escribir un programa que pida un número por teclado y nos imprima la tabla de
multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el
resultado será algo así:
74 x 1 = 74
74 x 2 = 148
…
74 x 10 = 740
"""

numero=int(input("Introduce el numero para saber su tabla: "))
for i in range(1,11):
    print( numero," X ", i," = ",numero*i)