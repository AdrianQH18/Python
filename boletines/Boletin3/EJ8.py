"""
Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.
"""
texto=input("Introduce tu texto: ")
vocales="aeiouAEIOU"
textoFinal=""
for letra in texto:
    if letra not in vocales:
        textoFinal+=letra
print(textoFinal)