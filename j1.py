num1=1
num2=2
print("La suma de los 2 numeros es: ", num1+num2)
# hola este es un comentario de una sola linea
"""comentario para mas de una linea""";
edad=56
print(edad)
edad="hola bebe"
print(edad)

#las cadenas de texto son tratadas como arrays
cadena1="HOLA MUNDO"
print(cadena1[0])

"""los operadores que se pueden usar son
=,+,-,*,/,%,//,**
+=,-=,*=,/=,%=
"""
x=2*2
x*=2
print(x)

#convertiendo una variable numerico a un variable de texto
precio=5.2
print(precio)
precio2=int(precio)
print(precio2)


#input
nombre=input("Inserta tu nombre: ")
apellidos=input("Inserta tus apellidos: ")
edad=input("Inserta tu edad: ")
print("Tu nombre y tu edad son: ",nombre,apellidos,"y tienes",edad,"años")