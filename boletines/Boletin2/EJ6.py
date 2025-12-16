"""
6. Modifica el ejercicio anterior para que la nota del boletín se redondee
matemáticamente si es superior a 5 pero se trunquen los decimales si es inferior a 5
"""
trabajo=float(input("Ingrese la nota de trabajo en clase: "))
ejercicios=float(input("Ingrese la nota de Ejercicios practicos: "))
examen=float(input("Ingrese la nota de Examen: "))

notaReal=(trabajo*0.05)+(ejercicios*0.15)+(examen*0.80)
print("Nota real: ",round(notaReal,2))
if notaReal >=5:
    notaBoletin=round(notaReal)
    print("Boletin: ",notaBoletin)
else:
    notaBoletin = int(notaReal)
    print("Boletin: ", notaBoletin)