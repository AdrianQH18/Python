"""
Escribir un programa que pida por teclado una cadena de texto y la separe en dos
distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la
segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe Hola
Mundo la primera cadena sería Hl ud y la segunda oaMno
"""
texto=input("Introduce tu texto: ")
letrasPar=""
letrasImpar=""
for i in range(len(texto)):
    if i%2==0:
        letrasPar+=texto[i]
    else:
        letrasImpar+=texto[i]
print(letrasPar)
print(letrasImpar)