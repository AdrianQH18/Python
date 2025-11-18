"""
nombre="Jose Maria"
edad=57
sueldo=1200.567
print("Mi nombre es", nombre,"tengo", edad,"años y cobro", sueldo, "euros")
print("Mi nombre es %s tengo %d años y cobro %.2f euros " %(nombre,edad,sueldo))
print(f"Mi nombre es {nombre} tengo {edad} años y cobro {sueldo} euros")
promedio=0.86754
print(f"El porcfentaje de aprobados es de {promedio:.4%}")
poblacion=1234567890
print(f"La poblacion del pais es de {poblacion:,} habitantes")
n1=23
n2=456
n3=1
print(f"Numeros:\n{n1:04d}\n{n2:04d}\n{n3:04d}")
print(f"Justificado a la izquierda: ***{n1:<20}***")
print(f"Justificado a la derecha  : ***{n1:>20}***")
print(f"Justificado al centro     : ***{n1:^20}***")
"""


#nombre="Jose Maria"
#edad =57
#sueldo=1200.567
#ficha=f"""
#==========================
#Nombre: {nombre}
#Edad: {edad}
#Sueldo {sueldo:.2f} euros
#==========================
#"""
#print(ficha)



def devuelveMiNombre():
    nobre="Jose Maria"