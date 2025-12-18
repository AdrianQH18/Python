# 3. Escribir un programa que cuenta las palabras que tiene una frase introducida
# previamente por teclado. Las palabras pueden estar separadas por más de un espacio
# pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
# puntuación como separadores.

count = 1  # a aa a
frase = str(input("Ejercicio 3: Introduce una frase: "))
for _ in range(0, len(frase)):
    if frase[_] == " ":
        count += 1
print(f"El numero de palabras es de {count}")