"""
Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
que ha encontrado y suprimido.
"""
texto=input("Introduce el texto: ")
contador=texto.count(" ")
textoSinEspacio=texto.replace(" ","")
print(textoSinEspacio)