#Escribir un programa que pida un número por teclado al usuario que simule ser el precio
#de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado debe de
#estar redondeado a dos decimales.
precio=int(input("Introduce un numero que sera el precio del producto"))
iva=precio*0.21
precioIva=precio+iva
print(round(precioIva,2))