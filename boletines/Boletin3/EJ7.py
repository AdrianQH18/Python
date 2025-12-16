"""
Escribir un programa que pida por teclado una cadena de texto y la escriba con el
alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
tengas en cuenta que además podrían ir acentuadas
"""
texto=input("Introduce tu texto: ")
textoHacker=texto.lower()
textoHacker=textoHacker.replace("a","4")
textoHacker=textoHacker.replace("e","3")
textoHacker=textoHacker.replace("i","1")
textoHacker=textoHacker.replace("o","0")

print(textoHacker)