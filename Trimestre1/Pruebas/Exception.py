"""
print("Inicio del programa")
try:
    denominador=int(input("Introduce el denominador: "))
    x=45/denominador
    print(x)
except ZeroDivisionError:
    print("No se puede dividir en cero")
except ValueError:
    print("No se puede convertir a entero")
except:
    print("Exception no encontrada")
else:
    print("Noa ha ocurrido ninguna exception")
finally:
    print("Haya o no Haya Expection")
print("FIN DEL PROGRAMA")
"""

"""
n=int(input("Introduce un numero entero positivo"))
if n<0:
    raise Exception("No es un entero positivo")
print(n)
"""

"""
n=int(input("Introduce un numero entero positivo"))
raise ZeroDivisionError("No has dividido por cero pero yo lo digo")
"""

n=int(input("Introduce un numero entero positivo"))
assert(n==1, "El numero no me gusta")