"""
3. Escribir un programa que pida un número por teclado al usuario que simule ser el
precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado
debe de estar redondeado a dos decimales.
"""

precio=int(input("Introduce el precio: "))
iva=precio*0.21
precioIva=precio+iva

print("Precio con iva: ",round(precioIva,2))