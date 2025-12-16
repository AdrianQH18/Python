#Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
#(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
#número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
#intereses de ningún tipo y redondeamos a dos decimales.
importe=float(input("Introduce el importe a pagar: "))
numMeses=int(input("Introduce el numero de meses que tenemos para pagar: "))

pago_por_mese=round(importe/numMeses,2)
print("Por mes debemos pagar un total de: ",pago_por_mese)